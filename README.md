Capstone AI Project - Gym-UnrealCV: Leveraging Deeper Involvement with Unreal 4
===
Disclaimer: 

This project relies heavily on the hard work and dedication of the teams behind UnrealCV (https://github.com/unrealcv) and Gym-UnrealCV(https://github.com/zfw1226/gym-unrealcv). Their work creates the excellent interface between Unreal 4 and OpenAI Gym. 

## Contents

# 1. Disclaimer (Above)

# 2. Working Log

# 3. Capstone Proposal


## Working Log


Active training can be viewed at : https://www.twitch.tv/ajatodin










### Capstone Proposal

## Domain Background
Computer vision research and reinforcement learning have progressed considerably in recent years. Contemporary models have used computer vision to obtain workable datasets from screen images of popular video games or other programmed environments, which are then used to train and test agents via reinforcement learning. The ability to obtain consistent and yet complex test environments which naturally predispose themselves towards providing some type of enumerated score has made video games in general excellent for the task of developing reinforcement learning algorithms. Agents created in these environments show incredible promise as well as real-world applications.
As such, numerous teams have worked to link game developer environments with reinforcement learning libraries. While there are many options in existence, one of the most advanced ones to date is UnrealCV. Used to develop moving and object tracking agents in the Unreal environment (https://arxiv.org/abs/1609.01326), this represents an advanced computer vision interface with extensible interaction options. Development in this regard is personally relevant as development in the Unreal Engine was the initial step in my own interest in machine learning and artificial intelligence. The ability to field agents that can act and react to players in video games and simulations beyond the confines of typically scripted game AI represents a giant leap forward for both the game industry, the simulation industry, and indeed, any sector which may see the benefits from being able to test complex AI in inexpensive and varied environments.
## Problem Statement
Current interaction with AI in a complex simulated setting has either been limited or ineffective to date. The current state of the art in terms of the game and simulation industry is primarily limited to AI scripted using Finite State Machines (FSMs) or behavior trees, both of which use sequences of events to determine the appropriate script to be used taking advantage of contexts provided by the game environment. Usage of reinforcement learning algorithms in complex game environments are typically not pursued by developers as they are considered extremely experimental and don't offer comparitive results to scripted AI when put head to head at defined tasks. Furthermore, the amount of complex environments available to machine learning engineers for iteration and development are still relatively limited, with few standards available to the wider community.
## Datasets and Inputs
The datasets presented are two levels created by the author in the Unreal Engine development environment, which is an open-source and free game engine offering simple development. Tying this engine to a python development environment is the plugin UnrealCV (created by Weichao Qiu, Fangwei Zhong, Yi Zhang, Siyuan Qiao,Zihao Xiao, Tae Soo Kim, Yizhou Wang, Alan Yuille), produced as an interface between Unreal Engine and OpenAI Gym. The inputs therein are a capture of the first-person view screen, natively showing as 640x480 images or video. From this dataset the agent has the choice of a number of defined inputs(http://docs.unrealcv.org/en/latest/reference/commands.html) as well as the extensible framework for additional inputs to mimic actual human player inputs. Any additional inputs (beyond visual representations) must be either presented in a visual manner or passed via a specialized runtime command. Given the scope of this proposal, the visual dataset and a means of visually representing the audio data will be presented and passed visually via the use of user interface elements.
## Solution Statement
I propose to develop an agent using CV and DDPG in order to interact credibly with the simulated environment. This agent will play in a simple, 1 versus 1 arena style shooter environment with a series of four opponents, a scripted AI, a Q-Learning agent developed inside the system environment (outlined by this paper: https://jewlscholar.mtsu.edu/bitstream/handle/mtsu/5247/BOYD%20%28Reece%29%20Final%20Thesis.pdf?sequence=1&isAllowed=y) as our benchmark model, a duplicate agent of itself, and finally, a human player. Following this test, and with development to ensure we have the most efficient agent given by this model, we will then compare the agent with the saved state and action spaces from the DDPG model to an agent with the same state and action spaces, but upgrade reward mechanisms. The final goal to this end will be an agent that is trained to play alongside a human controlled agent, and represents a credible improvement over a scripted AI agent.
## Benchmark Model
The benchmark with which we will be comparing our agent is the Q-Learning model created by Reece Boyd (see link above), which had reasonable performance for a Q-Learning agent given the short training periods, but was still subpar as compared to the scripted AI agent. This test will be considered a success if our agent can consistently outperform either the Q-Learning agent or the scripted agent, and represents an advantage when used as a teammate to a human player as compared to the Q-Learning agent and the scripted agent.
## Evaluation Metrics
The main metric used for this will be the "kill to death" ratio, a common metric utilized in online games. This is most demonstrated by the 1 versus 1 scenario. During the final team event, the metrics will expand to include, "friendly-fire kills", overall team performance, as well as a subjective rating system by which the human players that interact with each of the AI agents will rate them in terms of utility, with 4 being the highest rated partner, and 1 being the lowest rated partner. These results will be averaged between as many human players as we can reasonably gather for this play test and presented in order.
## Project Design
The initial step to completin this proposal is preparing the environment. For reproducability for other machine learning scientists, I anticipate creating a packaged binary game with the UnrealCV plugin. Once the environment is created, I will initially script an AI agent using the in-engine tools. Second, I will replicate Reece Boyd's Q-Learning agent.
Following that I will create the DDPG agent and begin training the agent. I anticipate a training progression from basic tasks to increasingly complex, as I feel that training the agent to compete initially in the arena will give subpar results. My approach to this training progression will be navigate a simple course (navigation and movement), "shooting" simulated targets with rewards allocated for enemy versus friendly targets appropriately, the training of tactics in response to stimuli, and finally the training of communicating to friendly agents (or humans), which in this case will be conducting using a visual feedback mechanism. This training approach mirrors that used by military organizations. As a comparitor, I intend to also train an agent for competition. I feel this will provide an excellent value comparison.
Finally, once the agent is trained, I will conduct the playtest comparing the agents in performance, finishing with the human agent cooperative tests. This will be considered the formal end to this proposal. I further intend to submit this pair of training scenarios, with the accompanying benchmarks to the UnrealCV Model Zoo, whereby they may be used for further development by other machine learning engineers.

if you have any suggestion or interested in using Gym-UnrealCV, get in touch at [zfw1226@gmail.com](zfw1226@gmail.com).



