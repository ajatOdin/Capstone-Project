# Machine Learning Engineer Nanodegree
## Capstone Proposal
Andrew Omernik
September 24th, 2018

## Proposal


### Domain Background


Computer vision research and reinforcement learning have progressed considerably in recent years. Contemporary models have used computer vision to obtain workable datasets from screen images of popular video games or other programmed environments, which are then used to train and test agents via reinforcement learning. The ability to obtain consistent and yet complex test environments which naturally predispose themselves towards providing some type of enumerated score has made video games in general excellent for the task of developing reinforcement learning algorithms. Agents created in these environments show incredible promise as well as real-world applications. 

As such, numerous teams have worked to link game developer environments with reinforcement learning libraries. While there are many options in existence, one of the most advanced ones to date is UnrealCV. Used to develop moving and object tracking agents in the Unreal environment (https://arxiv.org/abs/1609.01326), this represents an advanced computer vision interface with extensible interaction options. Development in this regard is personally relevant as development in the Unreal Engine was the initial step in my own interest in machine learning and artificial intelligence. The ability to field agents that can act and react to players in video games and simulations beyond the confines of typically scripted game AI represents a giant leap forward for both the game industry, the simulation industry, and indeed, any sector which may see the benefits from being able to test complex AI in inexpensive and varied environments. 

### Problem Statement
_(approx. 1 paragraph)_

Current interaction with AI in a complex simulated setting has either been limited or ineffective to date. The current state of the art in terms of the game and simulation industry is primarily limited to AI scripted using Finite State Machines (FSMs) or behavior trees, both of which use sequences of events to determine the appropriate script to be used taking advantage of contexts provided by the game environment. Usage of reinforcement learning algorithms in complex game environments are typically not pursued by developers as they are considered extremely experimental and don't offer comparitive results to scripted AI when put head to head at defined tasks. Furthermore, the amount of complex environments available to machine learning engineers for iteration and development are still relatively limited, with few standards available to the wider community.

### Datasets and Inputs
_(approx. 2-3 paragraphs)_

The datasets presented are two levels created by the author in the Unreal Engine development environment, which is an open-source and free game engine offering simple development. Tying this engine to a python development environment is the plugin UnrealCV (created by Weichao Qiu, Fangwei Zhong, Yi Zhang, Siyuan Qiao,Zihao Xiao, Tae Soo Kim, Yizhou Wang, Alan Yuille), produced as an interface between Unreal Engine and OpenAI Gym. The inputs therein are a capture of the first-person view screen, natively showing as 640x480 images or video. From this dataset the agent has the choice of a number of defined inputs(http://docs.unrealcv.org/en/latest/reference/commands.html) as well as the extensible framework for additional inputs to mimic actual human player inputs. Any additional inputs (beyond visual representations) must be either presented in a visual manner or passed via a specialized runtime command. Given the scope of this proposal, the visual dataset and a means of visually representing the audio data will be presented and passed visually via the use of user interface elements. 

### Solution Statement
_(approx. 1 paragraph)_

In this section, clearly describe a solution to the problem. The solution should be applicable to the project domain and appropriate for the dataset(s) or input(s) given. Additionally, describe the solution thoroughly such that it is clear that the solution is quantifiable (the solution can be expressed in mathematical or logical terms) , measurable (the solution can be measured by some metric and clearly observed), and replicable (the solution can be reproduced and occurs more than once).

### Benchmark Model
_(approximately 1-2 paragraphs)_

In this section, provide the details for a benchmark model or result that relates to the domain, problem statement, and intended solution. Ideally, the benchmark model or result contextualizes existing methods or known information in the domain and problem given, which could then be objectively compared to the solution. Describe how the benchmark model or result is measurable (can be measured by some metric and clearly observed) with thorough detail.

### Evaluation Metrics
_(approx. 1-2 paragraphs)_

In this section, propose at least one evaluation metric that can be used to quantify the performance of both the benchmark model and the solution model. The evaluation metric(s) you propose should be appropriate given the context of the data, the problem statement, and the intended solution. Describe how the evaluation metric(s) are derived and provide an example of their mathematical representations (if applicable). Complex evaluation metrics should be clearly defined and quantifiable (can be expressed in mathematical or logical terms).

### Project Design
_(approx. 1 page)_

In this final section, summarize a theoretical workflow for approaching a solution given the problem. Provide thorough discussion for what strategies you may consider employing, what analysis of the data might be required before being used, or which algorithms will be considered for your implementation. The workflow and discussion that you provide should align with the qualities of the previous sections. Additionally, you are encouraged to include small visualizations, pseudocode, or diagrams to aid in describing the project design, but it is not required. The discussion should clearly outline your intended workflow of the capstone project.

-----------

**Before submitting your proposal, ask yourself. . .**

- Does the proposal you have written follow a well-organized structure similar to that of the project template?
- Is each section (particularly **Solution Statement** and **Project Design**) written in a clear, concise and specific fashion? Are there any ambiguous terms or phrases that need clarification?
- Would the intended audience of your project be able to understand your proposal?
- Have you properly proofread your proposal to assure there are minimal grammatical and spelling mistakes?
- Are all the resources used for this project correctly cited and referenced?
