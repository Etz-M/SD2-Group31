"""
------------------------------------------------------------------------------
Senior Design : Group 31 : Spring 2024
Etzkiel Martinez, Daniel Price, Michael Montoya, Katheryn Berndt

Description : This script will provide the generic helper functions for 
              SelfLearning.py.

------------------------------------------------------------------------------
"""

def GatherTasks():
    """
    Gather the list of task that the model will learn from actions_to_be learned.txt

    Args:
        N/A

    Returns:
        tasks (str[]): the list of actions to train the model.
    """
    print("get tasks from actionstobelearned.txt")

    #create the list of tasks to learn from actions_to_be_learned.txt


def UpdateTasks(taskLearned, iterations):
    """
    Update the file containing the task that the model has to learn from actions_to_be_learned.txt 
    and note it down in actions_learned.txt.

    Args:
        taskLearned (str): the task that the model has learned.
        iterations (int): the number of iterations it took for the model to learn the action.

    Returns:
        tasks (str[]): the list of actions to train the model.
    """
    print("get tasks from actionstobelearned.txt")

    #find the task learned in actions_to_be_learned.txt

    #add it to actions_learned.txt

def CommandToArm():
    """
    Send the command to the ESP32 via UART

    Args:
        Command (str) : the command that will be sent
    
    Returns:
        N/A
    """
