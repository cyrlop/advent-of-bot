"""
Module to parse incoming text messages and choose an answer.
"""

import re
def respond_to_message(message):
    """Give a different response based on message received"""
    message_alnum = re.sub('[^A-Za-z0-9]+', '', message).lower()

    if message_alnum == "help":
        answer = get_help_answer()

    elif message_alnum == "about":
        answer = get_about_answer()

    elif message_alnum == "leave":
        answer = get_leave_answer()

    elif message_alnum == "whyamihere":
        answer = get_why_answer()

    else:
        answer = get_not_recognised_answer()

    return answer


#############################################
########## Pre-defined text
#############################################
def get_not_recognised_answer():
    answer = "This command was not recognised, try `help` to see available commands."
    return answer

def get_help_answer():
    answer = "```"
    answer += "===== Available commands ====="
    answer += "\n - 'help': display this message"
    answer += "\n - 'about': explain what this chat room is about"
    answer += "\n - 'leave': display the procedure to leave the room"
    answer += "\n - 'why am i here?': Will tell you why you are here"
    answer += "```"
    return answer

def get_about_answer():
    answer = "This group was originally created for community communication"
    answer += " around Advent of Code yearly open challenge https://adventofcode.com/2019/about"
    return answer

def get_leave_answer():
    btn_text = "\"Leave (you can always return)\""

    answer = "In order to leave, please:"
    answer += f"\n - *Google Chat App:* Click on the name of the chat and then {btn_text}"
    answer += f"\n - *GMail-Web:* Click on the 3 Dots and then again {btn_text}"
    return answer

def get_why_answer():
    answer = "No one really knows for sure, it might be a honest IT mistake,"
    answer += " a big troll, a social experiment. Now you can discuss with people"
    answer += " around the world about anything and have unexpected answers!"
    return answer
