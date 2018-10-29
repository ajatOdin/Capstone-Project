import os
import gym
import numpy as np
from gym import spaces
from gym_unrealcv.envs.navigation import reward, reset_point
from gym_unrealcv.envs.navigation.visualization import show_info
from gym_unrealcv.envs.utils import env_unreal
from gym_unrealcv.envs.navigation.interaction import Navigation
'''
It is a general env for searching target object.

State : raw color image and depth (640x480) 
Action:  (linear velocity ,angle velocity , trigger) 
Done : Collision or get target place or False trigger three times.
Task: Learn to avoid obstacle and search for a target object in a room, 
      you can select the target name according to the Recommend object list in setting files
      
'''
'''
Line 55 in example/ddpg/CriticNetwork.py
h2 = merge module object is not callable
'''
class Capstone_AIArena(gym.Env):
    def __init__(self,
                 setting_file,
                 reset_type='waypoint',  # testpoint, waypoint,
                 augment_env=None,  # texture, target, light
                 action_type='continuous',  # 'Discrete', 'Continuous'
                 observation_type='color',  # 'color', 'depth', 'rgbd'
                 reward_type='distance',  # distance, bbox, bbox_distance,
                 docker=False,
                 resolution=(640, 480)
                 ):
        
        setting = self.load_env_setting(setting_file)
        self.cam_id = setting['cam_id']
        self.target_list = setting['targets']#[category]
        self.trigger_th = setting['trigger_th']
        self.height = setting['height']
        self.pitch = setting['pitch']
        self.discrete_actions = setting['discrete_actions']
        self.continous_actions = setting['continous_actions']
        
        self.currentTargets = 0
        
        self.docker = docker
        self.reset_type = reset_type
        self.augment_env = augment_env

        # start unreal env
        self.unreal = env_unreal.RunUnreal(ENV_BIN=setting['env_bin'])
        env_ip, env_port = self.unreal.start(docker, resolution)

        # connect UnrealCV
        self.unrealcv = Navigation(cam_id=self.cam_id,
                                   port=env_port,
                                   ip=env_ip,
                                   targets=self.target_list,
                                   env=self.unreal.path2env,
                                   resolution=resolution)
        self.unrealcv.pitch = self.pitch

        #  define action
        self.action_type = action_type
        
        try:
            assert self.action_type == 'discrete' or self.action_type == 'continuous'
        except AssertionError:
            print('action_type is throwing an error in Unreal Capstone.py')
            print('Action Type : ', self.action_type)
        if self.action_type == 'discrete':
            print('Def a discrete action')
            self.action_space = spaces.Discrete(len(self.discrete_actions))
        elif self.action_type == 'continuous':
            self.action_space = spaces.Box(low=np.array(self.continous_actions['low']),
                                           high=np.array(self.continous_actions['high']))

        # define observation space,
        # color, depth, rgbd,...
        self.observation_type = observation_type
        print(self.observation_type, 'Obvs Type')
        try: 
            assert self.observation_type == 'color' or self.observation_type == 'depth' or self.observation_type == 'rgbd'
        except AssertionError:
            print('self.observation_type is throwing an error in Unreal Capstone.py')
            print('Observation Type : ', self.observation_type)
        self.observation_space = self.unrealcv.define_observation(self.cam_id,self.observation_type, 'direct')
        #self.observation_space = self.unrealcv.define_observation(self.cam_id, self.observation_type, 'direct')
        
        #Input Channel (which pulls from Observation Space) is returning nothing as a response. 
        
        
        
        # define reward type
        #this needs to be replaced with the evolutionary reward function
        #transitioning rewards from look aim to movement, to communication
        # distance, bbox, bbox_distance, look aim
        self.reward_type = reward_type
        self.reward_function = reward.Reward(setting)

        # set start position
        self.trigger_count = 0
        current_pose = self.unrealcv.get_pose(self.cam_id)
      
        current_pose[2] = self.height
        self.unrealcv.set_location(self.cam_id, current_pose[:3])
        
        self.count_steps = 0

        self.targets_pos = self.unrealcv.build_pose_dic(self.target_list)
        self.currentTargets = len(self.target_list)
        # for reset point generation and selection
        self.reset_module = reset_point.ResetPoint(setting, reset_type, current_pose)

    def _step(self, action ):
        info = dict(
            Collision=False,
            Done=False,
            Trigger=0.0,
            Reward=0.0,
            Action=action,
            Bbox=[],
            Pose=[],
            Trajectory=self.trajectory,
            Steps=self.count_steps,
            Target=[],
            Direction=None,
            Waypoints=self.reset_module.waypoints,
            Color=None,
            Depth=None,
        )
        
        fire_threshold = 0.4
        
        action = np.squeeze(action)
        if self.action_type == 'discrete':
            print('action : ', action)
            
            print('Trigger 1', info['Trigger'])
            (velocity, angle, info['Trigger']) = self.discrete_actions[action]
        else:
            (pitch, yaw, x2d, y2d, fire) = action
            #(velocity, angle, info['Trigger']) = action
        self.count_steps += 1
        info['Done'] = False
        #take action
        #aiming aspect
        
        # Action Needs to refer to :
        #QAdjust Statespace in Settings.json

        # Pitch and Yaw for aiming
        # Movement (Forward, Back, Left, Right)
        # Firing Weapon (should this equal a trigger or no?)
        #Do we even need a trigger? Or should we return health / ammo as a stat? How to return through UnrealCV
        #Part of the question is what does a trigger threshold equal?
        #Reward function for first iteration should focus on minimal movement, aiming towards targets, and firing and hitting targets
        #Three different reward functions
        # 1. Aim and shoot + Highlight? Also need friendly bots in (blue) named different in Unreal to account for FF
        #   Closer a rotation is to enemy higher minute reward, firing gets points for kills, highlighting Good for small bit
        # 3. Move and engage enemies
        # Constant movement is a reward, killed enemies are large reward
        # 4. Highlight seen enemies for team
        # 5. Fight!!!
        #Question is whether to punish AI for missed shots (may dissuade from shooting)

        #Second is being able to save our state space and reupload it
        
        print('Trigger_TH is : ', self.trigger_th, 'Trigger Response is : ', info['Trigger'])
        
        # take action
        if self.action_type == 'discrete':
            #Handle Collision Detection
            info['Collision'] = self.unrealcv.move_2d(self.cam_id, angle, velocity)
            info['Pose'] = self.unrealcv.get_pose(self.cam_id, 'soft')
        else:
            #All of our continuous state/action space goes here
            info['Collision'] = move_character(self, cam_id, x2d, y2d):
            lookSuccess = look_3d(self.cam_id, yaw, pitch)
            if (fire > fire_threshold):
                fireSuccess = fire_weap(fire)
            
        #Functions are built for shot reward. Need to include functions calls here and handle the trigger thing
        
        
            
            
            #info['Collision'] = self.unrealcv.move_2d(self.cam_id, angle, velocity)
        # the robot think that it found the target object,the episode is done
        # and get a reward by bounding box size
        # only three times false trigger allowed in every episode
        #Reward Calls below:
        
        '''
        if info['Trigger'] > self.trigger_th:
            self.trigger_count += 1
            # get reward
            if 'bbox' in self.reward_type:
                object_mask = self.unrealcv.read_image(self.cam_id, 'object_mask')
                boxes = self.unrealcv.get_bboxes(object_mask, self.target_list)
                info['Reward'], info['Bbox'] = self.reward_function.reward_bbox(boxes)
            else:
                info['Reward'] = 0

            if info['Reward'] > 0 or self.trigger_count > 3:
                info['Done'] = True
                if info['Reward'] > 0 and self.reset_type == 'waypoint':
                    self.reset_module.success_waypoint(self.count_steps)
           
        else:
            # get reward
            distance, self.target_id = self.select_target_by_distance(info['Pose'][:3], self.targets_pos)
            info['Target'] = self.targets_pos[self.target_id]
            info['Direction'] = self.get_direction(info['Pose'], self.targets_pos[self.target_id])

            # calculate reward according to the distance to target object
            if 'distance' in self.reward_type:
                info['Reward'] = self.reward_function.reward_distance(distance)
            else:
                info['Reward'] = 0

            # if collision detected, the episode is done and reward is -1
            if info['Collision']:
                info['Reward'] = -1
                info['Done'] = True
                if self.reset_type == 'waypoint':
                    self.reset_module.update_dis2collision(info['Pose'])
        '''
        
        
        
        # update observation
        state = self.unrealcv.get_observation(self.cam_id, self.observation_type)
        info['Color'] = self.unrealcv.img_color
        info['Depth'] = self.unrealcv.img_depth

        # save the trajectory
        self.trajectory.append(info['Pose'][:6])
        info['Trajectory'] = self.trajectory
        if info['Done'] and len(self.trajectory) > 5 and self.reset_type == 'waypoint':
            self.reset_module.update_waypoint(info['Trajectory'])

        return state, info['Reward'], info['Done'], info

    def _reset(self, ):

        # double check the resetpoint, it is necessary for random reset type
        collision = True
        
        resetCounter = 0
        while collision:
      
            current_pose = self.reset_module.select_resetpoint()
            self.unrealcv.set_pose(self.cam_id, current_pose)
            collision = self.unrealcv.move_2d(self.cam_id, 0, 100)
            resetCounter+=1
            if resetCounter >= 10:
                self._close()
                break
        self.unrealcv.set_pose(self.cam_id, current_pose)
   
        state = self.unrealcv.get_observation(self.cam_id, self.observation_type)

        self.trajectory = []
        self.trajectory.append(current_pose)
        self.trigger_count = 0
        self.count_steps = 0
        self.reward_function.dis2target_last, self.targetID_last = \
            self.select_target_by_distance(current_pose, self.targets_pos)
        return state

    def _seed(self, seed=None):
        return seed

    def _render(self, mode='rgb_array', close=False):
        if close==True:
            self.unreal.close()
        return self.unrealcv.img_color
    def check_targets(self):
        targetNum = len(self.target_list)
        missingObj = 0
        foundObj = 0
        objs = self.unrealcv.get_objects()
        for target in self.target_list:
            if target in objs:
                foundObj+=1
            else:
                missingObj+=1
        print([foundObj, missingObj])
        return([foundObj, missingObj])
        
    def _close(self):
        self.unreal.close()

    def _get_action_size(self):
        return len(self.action)

    def select_target_by_distance(self, current_pos, targets_pos):
        # find the nearest target, return distance and targetid
        target_id = list(self.targets_pos.keys())[0]
        distance_min = self.unrealcv.get_distance(targets_pos[target_id], current_pos, 2)
        for key, target_pos in targets_pos.items():
            distance = self.unrealcv.get_distance(target_pos, current_pos, 2)
            if distance < distance_min:
                target_id = key
                distance_min = distance
        return distance_min, target_id

    def get_direction(self, current_pose, target_pose):
        y_delt = target_pose[1] - current_pose[1]
        x_delt = target_pose[0] - current_pose[0]
        angle_now = np.arctan2(y_delt, x_delt)/np.pi*180-current_pose[4]
        if angle_now > 180:
            angle_now -= 360
        if angle_now < -180:
            angle_now += 360
        return angle_now

    def load_env_setting(self, filename):
        import gym_unrealcv

        gympath = os.path.dirname(gym_unrealcv.__file__)
        gympath = os.path.join(gympath, 'envs/setting', filename)
        f = open(gympath)
        filetype = os.path.splitext(filename)[1]
        if filetype == '.json':
            import json
            setting = json.load(f)
        else:
            print ('unknown type')

        return setting
''' Trial work for discrete actions
"discrete_actions": [
		[30,  0,  0,  0,  0],
		[0,  30,  0,  0,  0],
		[0, -30,  0,  0,  0],
		[0,   0, 20,  0,  0],
		[0,   0,-20,  0,  0],
		[0,   0,  0,  0,  1]
	],


'''
