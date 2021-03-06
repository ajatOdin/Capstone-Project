import unrealcv
import numpy as np
class Reward():
    '''
    define different type reward function
    '''
    def __init__(self, setting):
        self.reward_factor = setting['reward_factor']
        self.reward_th = setting['reward_th']
        self.dis2target_last = 0
    def angle_between(v1, v2):
    """Finds angle between two vectors"""
        v1_u = unit_vector(v1)
        v2_u = unit_vector(v2)        
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
    
    def lookaim(self, selfposition, objects):
        #Compare object rotation with character rotation
        AimSum = 0
        reward = 0
        agentRot = get_rotation(self, 0)
        for obj in objects:
            #Compare needed vector with current vect0r, interpolate reward from that
            npRot = angle_between(selfposition, unrealcv.get_obj_location(obj))
            print('Rotation in lookAim is : ', npRot)
            print('AgentRot is : ', agentRot)
        
        return reward
    def fireat(self, selfposition, changeInObjects):
        AimSum = 0
        reward = 0
        if changeInObjects>0:
            reward+=changeInObjects*5
        agentRot = get_rotation(self, 0)
        for obj in objects:
            #Need to count the objects and compare with a known start object count. 
            #Compare needed vector with current vect0r, interpolate reward from that
            npRot = angle_between(selfposition, unrealcv.get_obj_location(obj))
            print('Rotation in lookAim is : ', npRot)
            print('AgentRot is : ', agentRot)
        
        
    def reward_bbox(self, boxes):
        reward = 0

        # summarize the reward of each detected box
        for box in boxes:
            reward += self.get_bbox_reward(box)

        if reward > self.reward_th:
            # get ideal target
            reward = min(reward * self.reward_factor, 10)
        elif reward == 0:
            # false trigger
            reward = -1
        else:
            # small target
            reward = 0

        return reward, boxes

    def get_bbox_reward(self, box):
        # get reward of single box considering the size and position of box
        (xmin, ymin), (xmax, ymax) = box
        boxsize = (ymax - ymin) * (xmax - xmin)
        x_c = (xmax + xmin) / 2.0
        x_bias = x_c - 0.5
        discount = max(0, 1 - x_bias ** 2)
        reward = discount * boxsize
        return reward

    def reward_distance(self, dis2target_now):
        reward = (self.dis2target_last - dis2target_now) / max(self.dis2target_last, 100)
        self.dis2target_last = dis2target_now

        return reward
