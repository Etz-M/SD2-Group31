"""
------------------------------------------------------------------------------
Senior Design : Group 31 : Spring 2024
Etzkiel Martinez, Daniel Price, Michael Montoya, Katheryn Berndt

Description : This script will provide SelfLearning.py with the helper functions
  that it needs for training the model. It will include utilities such as: training
  the model based upon given feedback, provided the model with the necessary 
  information that it will need to commence training, and etc.
  
  The approach this script takes is to provide the model with string prompts for 
  evaluation and training. The idea is to rely on the model's coherence and problem-solving
  capabilities. This would abstract typical ML principles such as not needing to compute
  loss and adjust weights into a format that simply relies on evaluating the model and then
  providing positive or negative feedback.

------------------------------------------------------------------------------
"""

def InitiateTrainingContext():
    """
    Will train the model with the context needed to begin generating attempts to accomplish task.

    Args:
        TODO

    Returns:
        TODO
    """
    print("TODO: Give the model some context by training it on what is should attempt \
          to accomplish ")
    prompt = ""
    FineTuneModel(prompt)

    #need to figure out how to initiate LLaMA by looking at the provided code from Meta. (i have locally)

#may be redundant with FineTuneModel() and ReinforceModel()
def FineTuneModel(prompt):
    """
    Train the model's weights based upon the given prompts

    Args:
        prompt (str) - the message to train the model with.

    Returns:
        TODO
    """
    print("TODO: training function, will actually train the model.")
    #need to watch the video on using the fine-tuning framework


def ReinforceModel():
    """
    Provide the model with the passed in feedback. (MAY NOT BE NECESSARY IF I CAN REINFORCE DURING FINE TUNING)

    Args:
        feedback(str) : what to tell the model.

    Returns:
        nextStep (str?) : should the model continue training, move on the next command,
                        or end training (NOTE: may not be handled here)
    """
    print("TODO: train llama based on positive or negative feedback")

def EvaluateModel(task, currentPosition):
    """
    Have the model generate a prompt to attempt to complete current task at hand.

    Args:
        task (str) : the task that is currently being evalutated.
        currentPostion (str) : the current position of the robotic arm. #MAY BE IN THE FORM OF AN INT
    
    Returns:
        response (str) : response from the model.
    """
    # generate the prompt
    strToModel = "The current position of " + currentPosition + ". " + task

    #TODO: send the prompt to the model
    # --------------------------- NEED TO FIGURE OUT SEND PROMPTS TO LLAMA ---------------------------

    #return the response





def PositiveReinforcement():
    """
    Form a cohesive prompt to be sent to the model in the fine-tuning stage
    formatted as a positive reinforcement message.

    Args:
        result (str) : a description of what happened (output from CV function).
        action (str) : the action that the model is to learn, will be sent to the model as a reminder.

    Returns:
        message (str) : the concatenated string that will be sent to the model.
    """
    print("TODO: generated the string that will be given to llama as positive feedback")



def NegativeReinforcement():
    """
    Form a cohesive prompt to be sent to the model in the fine-tuning stage
    formatted as a negative reinforcement message.

    Args:
        result (str) : a description of what happened (output from CV function).
        action (str) : the action that the model is to learn, will be sent to the model as a reminder.

    Returns:
        message (str) : the concatenated string that will be sent to the model.
    """
    print("TODO: generated the string that will be given to llama as Negative feedback")
