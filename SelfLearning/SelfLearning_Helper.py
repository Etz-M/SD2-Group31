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

    tasks = []
    #create the list of tasks to learn from actions_to_be_learned.txt
    with open("actions_to_be_learned.txt", "r") as file:
        for line in file:
            tasks.append(line)
    
    #data preprocessing
    tasks = [task.strip() for task in tasks]
    
    print("[INFO] Grabbed tasks from actionstobelearned.txt")
    return tasks


def UpdateTasks(tasks, taskLearned, iterations):
    """
    Update the file containing the task that the model has to learn from actions_to_be_learned.txt 
    and note it down in actions_learned.txt.

    Args:
        tasks (str[]): the current list of actions to train the model.
        taskLearned (str): the task that the model has learned.
        iterations (int): the number of iterations it took for the model to learn the action.

    Returns:
        updatedTasks (str[]): the updated lists of actions to train the model.
    """
    
    #remove task learned from current list of tasks
    tasks.remove(taskLearned)

    #find the task learned in actions_to_be_learned.txt
    # with open("actions_to_be_learned.txt", "r") as file:
    #     oldTasks = file.readlines()

    # #remove the task from tasks array
    # for t in oldTasks:
    #     if t == taskLearned:
    #         oldTasks.remove(t)
    #         break

    #write the updated tasks to actions_to_be_learned.txt
    with open("actions_to_be_learned.txt", "w") as file:
        for t in tasks:
            file.write(t +"\n")
       
    #add task to to actions_learned.txt
    updateStr = taskLearned + "\t - " + str(iterations) + " iterations"
    with open("actions_learned.txt", "a") as file:
        file.write(updateStr + "\n")

    print("[INFO] Removed " + taskLearned + " from actions_to_be_learned.txt \n\t \
            and added \"" + updateStr + "\" to actions_learned.txt\n")
    return tasks


def CommandToArm_Linux():
    """
    Send the command to the ESP32 via UART

    Args:
        Command (str) : the command that will be sent
    
    Returns:
        N/A
    """
