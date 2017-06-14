ENV_NAME = 'Unrealcv-Search-v3'

CONTINUE = False #load a pre-trained model
RESTART_EP = 1800 # the episode number of the pre-trained model

TRAIN = True # train the network
USE_TARGET_NETWORK = False # use the target network
SHOW = True # show the current state, reward and action
MAP = False # show the trajectory in 2d map

MAX_EPOCHS = 100000 # max episode number

MEMORY_SIZE = 10000
LEARN_START_STEP = 5000
INPUT_SIZE = 150
INPUT_CHANNELS = 3
BATCH_SIZE = 64
LEARNING_RATE = 1e-3  # 1e6
GAMMA = 0.95
INITIAL_EPSILON = 1  # starting value of epsilon
FINAL_EPSILON = 0.1  # final value of epsilon
MAX_EXPLORE_STEPS = 5000
TEST_INTERVAL_EPOCHS = 100
SAVE_INTERVAL_EPOCHS = 200

MONITOR_DIR = 'log-basev3/monitor/' #the path to save monitor file
MODEL_DIR = 'log-basev3/model' # the path to save deep model
PARAM_DIR = 'log-basev3/param' # the path to save the parameters
TRA_DIR = 'log-basev3/trajectory.csv' # the path to save trajectory

#the path to reload weights, monitor and params
weights_path = 'log-nodis/model/dqn_ep' + str(RESTART_EP)+ '.h5'
monitor_path = 'log-nodis/monitor/'+ str(RESTART_EP)
params_json = 'log-nodis/param/dqn_ep' + str(RESTART_EP) + '.json'
