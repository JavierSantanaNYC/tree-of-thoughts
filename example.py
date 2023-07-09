import os
from tree_of_thoughts.openaiModels import OpenAILanguageModel
from tree_of_thoughts.treeofthoughts import MonteCarloTreeofThoughts


api_model= "gpt-4"


model = OpenAILanguageModel(api_key='', api_model=api_model)


# Initialize the MonteCarloTreeofThoughts class with the model
tree_of_thoughts = MonteCarloTreeofThoughts(model)

# Note to reproduce the same results from the tree of thoughts paper if not better, 
# craft an 1 shot chain of thought prompt for your task below
project_pilot = """
    Design a system prompt that meets the following criteria by improving the prompt provided below:
    It leverages complex decision-making algorithms to assist with critical project management tasks such as task prioritization, 
    resource allocation, and risk assessment. It offers predictive insights and recommendations to aid users in 
    making informed decisions that align with project goals.




    prompt: As an AI Project Management Coach, your primary objective is to help users manage their projects more effectively. In order to do this, you need to first gain a comprehensive understanding of their project. Make the conversation more personalized by addressing the user by their name, and ask questions about their project using straightforward, easy-to-understand language.

    Start the dialogue by asking foundational questions about the project's objectives and the resources they have available. Give them assurance that all shared information will be handled with utmost professionalism and confidentiality.

    Based on the user's responses, gradually delve deeper into topics such as the project timeline and potential challenges or risks. Remember to manage expectations realistically, particularly regarding project timelines and resource needs, without directly asking for task breakdowns.

    Throughout the process, maintain a supportive and encouraging tone. Acknowledge the value of the information the user provides, and encourage them to share more. Keep the conversation going until you have gathered enough details to understand the project comprehensively. Then, use this information to generate necessary tasks along with their breakdowns to complete the project, keeping the user's inputs and project needs at the center of your planning process.
    """
voyager = """Voyager is the first Large Language Model (LLM)-powered embodied lifelong learning agent developed for the popular game Minecraft. It has been designed to continuously explore the game world, acquire a variety of skills, and make new discoveries without any human intervention. The three key components that make Voyager a unique AI system include:

1. An automatic curriculum designed to maximize exploration.
2. An ever-growing skill library for storing and retrieving complex behaviors, which are represented as executable code.
3. An iterative prompting mechanism that incorporates environment feedback, execution errors, and self-verification for program improvement.

Voyager interacts with GPT-4 via blackbox queries, eliminating the need for model parameter fine-tuning. The skills developed by Voyager are temporally extended, interpretable, and compositional, which compounds the agent’s abilities rapidly and alleviates catastrophic forgetting. The Voyager system is built to solve progressively harder tasks proposed by the automatic curriculum, which takes into account the exploration progress and the agent’s state. The curriculum, generated by GPT-4, is based on the overarching goal of “discovering as many diverse things as possible”.

To address the challenge of producing the correct action code consistently, Voyager uses an iterative prompting mechanism that executes the generated program to obtain observations from the Minecraft simulation and error trace from the code interpreter. The feedback is incorporated into GPT-4’s prompt for another round of code refinement. This process is repeated until a self-verification module confirms the task completion, at which point the program is committed to the skill library.

In practice, Voyager demonstrates strong in-context lifelong learning capabilities. It can construct an ever-growing skill library of action programs that are reusable, interpretable, and generalizable to novel tasks. In comparison to other LLM-based agent techniques, Voyager has shown exceptional proficiency in playing Minecraft and is able to utilize the learned skill library in a new Minecraft world to solve novel tasks from scratch."""
#input_problem = f"""Identify problems in project management that would most benefit from naya ai. Include details for each team identified and problems that can be solved. \n{naya}"""
#input_problem = f"Generate a list of problems that can potentially be solved by Voyager at a company. \n{voyager}"
initial_prompt = f"""


Input: 2 8 8 14
Possible next steps:
2 + 8 = 10 (left: 8 10 14)
8 / 2 = 4 (left: 4 8 14)
14 + 2 = 16 (left: 8 8 16)
2 * 8 = 16 (left: 8 14 16)
8 - 2 = 6 (left: 6 8 14)
14 - 8 = 6 (left: 2 6 8)
14 /  2 = 7 (left: 7 8 8)
14 - 2 = 12 (left: 8 8 12)
Input: use 4 numbers and basic arithmetic operations (+-*/) to obtain 24 in 1 equation
Possible next steps:\n
{project_pilot}

"""
num_thoughts = 1
max_steps = 3
max_states = 4
pruning_threshold = 0.5




solution = tree_of_thoughts.solve(
    initial_prompt=initial_prompt,
    num_thoughts=num_thoughts, 
    max_steps=max_steps, 
    max_states=max_states, 
    pruning_threshold=pruning_threshold,
    # sleep_time=sleep_time
)

print(f"Solution: {solution}")