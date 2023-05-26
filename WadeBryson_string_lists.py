"""
Author: Wade Bryson
"""

# imports first
import random

# Setting up logger
from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# Task 4 - Setting up some string lists
player_names = ["Hayden", "Collin", "Gunner", "Jacob", "Andrew", "Jacob", "Wyatt", "Koven"]
shot_types = ["slam dunk", "contested layup", "free throw", "three pointer", "half-court shot"]
shot_descriptors = ["swished", "banked", "rattled in", "nailed"]
opponents_names = ["Miami", "Boston", "Los Angeles", "New York", "Cleveland", "Miami", "Chicago", "Boston"]
opponents_mascots = ["Heat", "Celtics", "Lakers", "Knicks", "Cavaliers", "Bulls"]

# Task 4 Lists 1 - Use the len(), set(), and zip() to combine two tuples
# Find a set of unique opponents names
unique_opp_names = set(opponents_names)
# Using zip() that combines an opponents name and their mascot
combined_names = zip(unique_opp_names, opponents_mascots)
printable_combined_names = list(combined_names)

# Loggin all the info
logger.info(f"Here is your list of opponents you played this year: {opponents_names}.")
logger.info(f"Here is your list of unique opponents you played this year: {unique_opp_names}.")
logger.info(f"Here is your list of unique opponents mascots you played this year: {opponents_mascots}.")
logger.info(f"Here is your list of opponents and their mascots combined together: {printable_combined_names}")
logger.info(f"Oops I made a mistake! Let me correct that!")
# Function that removes duplicates from a list and preserves order. Found on geeksforgeeks.org .
def removeduplicate(data):
    countdict = {}
    for element in data:
        if element in countdict.keys():
             
            # increasing the count if the key(or element)
            # is already in the dictionary
            countdict[element] += 1
        else:
            # inserting the element as key  with count = 1
            countdict[element] = 1
    data.clear()
    for key in countdict.keys():
        data.append(key)
# Running the function
removeduplicate(opponents_names)
# Using zip() to creat a correct combination of opponents name and their mascot
correct_combined_names = zip(opponents_names, opponents_mascots)
print_friendly_names = list(correct_combined_names)
# Logging the new info
logger.info(f"Does this look better?")
logger.info(f"Here is the correct list of opponents and their mascots combined together: {print_friendly_names}")

# Task 4 Lists 2 - Random Choice
# Creating a random sentence using my lists
# This sentence will be a random statement about a player on my team making a game winning shot to beat another team.
sentence = (
        f"{random.choice(player_names)} {random.choice(shot_descriptors)} a {random.choice(shot_types)} at the buzzer to defeat the {random.choice(print_friendly_names)}!!!!"
    )
# Logging the sentence
logger.info(f"Random sentence: {sentence}")

# Task 4 Lists 3 - Get unique words
# Found a free basketball text file on GitHub but I could not get it work for some reason. I used the Zen of Python text file instead
# Opening the text file
full_text = open("text_zen_of_python.txt")
# Reading and logging the file
read_full_text = full_text.read()
logger.info(f"{read_full_text}")
# Creating a list of the strings in the text file
text_list = read_full_text.split()
# Find the unique words in the text file
unique_text_list = set(text_list)
# Order the unqie list alphabetically
alpha_text_list = sorted(unique_text_list)
numb_words = len(alpha_text_list)
# Logging the number of words and the alphabetically list
logger.info(f"Here is a list of the {numb_words} unique words in the Zen of Python file: {alpha_text_list}")

# Print the logged information
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())





