"""
------------------------------------------------------------------------------
Senior Design : Group 31 : Spring 2024
Etzkiel Martinez, Daniel Price, Michael Montoya, Katheryn Berndt

Description : This script will contorl the flow of the self-learning process 
  for fine-tuning LLaMa using reinforcement learning principles. This script
  will call functions declared in helper scripts that will handle the intermediary
  steps of the training.

  The use of this script will be generic. This script will repeatively provide the
  LLM with the task it meant to learn then provide response on what has happened.

  For the self-learning robotic arm use case, the model will be given initial context 
  on what is going on and what it is trying to learn. It will then be given an task from
  a list of actions from "actions_to_be_learned.txt" that it will attempt to learn.
  Then, the model will repeatively generate prompts and will be given a response of what happened.
  If it failed, it will try again. If it succeeded, it will be told that it succeeded, and will
  congragulated and will move on to the next task to learn if there is one. Otherwise, 
  program will end.

------------------------------------------------------------------------------
"""

from SelfLearning_Helper import *
from TrainingLLM import *
from LLMEyes import *

print("--------------------- Hello llama ---------------------")

#Gather actions to be learned
tasks = GatherTasks()
# print(tasks)

# tasks = UpdateTasks(tasks, tasks[3], 10)
# print(tasks)
# tasks = UpdateTasks(tasks, tasks[1], 10)
# print(tasks)


# Instantiate the model (TODO)



'''
Begin with the initial training of the model, purposed with giving the model some 
  context of what it is being trained on and what its objective is.
  NOTE: only necessary if this is the first time running the script or training the 
        the model at relavent task (AKA continueing prior training). Otherwise, comment the line out.
'''

'''
InitiateTrainingContext()

#keep track of number of training iterations
iterations = 0
success = False

# Begin trainging the model, one task at a time.
for task in tasks:

    while (success == False):
        # Prompt the model with the current task to learn.
        print("Prompting the model with " + task)
        response = EvaluateModel(task)
        
        #send the command to the arm
        print("Model generated: " + response)
        CommandToArm_Linux(response)

        #Recieve what happened from the computer vision software
        #   NOTE: will perhaps have to implement some kind of wait/sleep/asynchronous
        #           feature that will wait for the arm to move and such.
        #   NOTE: maybe will be the same for waiting for the model to generate a command/response
        result = WhatHappened()

        #check if the result matches what happened
        if (result == task):
            # success, tell model and move onto the next task
            
            #generate positive response and tell model
            reinforcementMessage = PositiveReinforcement(task)
            FineTuneModel(reinforcementMessage)

            # update statistics
            success = True
            UpdateTasks(task)   #keep track of what the model was able to accomplish.
        else:
            # fail, provide feedback to model and try again.

            reinforcementMessage = NegativeReinforcement(task)
            FineTuneModel(reinforcementMessage)
    
    #End of while, task learned. Try next task or end training.


'''

# Train the model to complete each of the tasks

# Begin repeatively evaluating the model on it ability to complete the objective at hand.


#NOTE: will have to first preprocess the response from the model to extract the hex code command
#   for the robotic arm. If the model generates an incoherent response, then it will be told to try again