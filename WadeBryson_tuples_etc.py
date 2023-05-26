"""
Author: Wade Bryson

Purpose: Demonstrate knowledge of tuples and dictionaries

Domain: Basketball
"""

# Setting up logger
from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# Creating some tuples
# Tuple setup = (Name, Position, Points per game)
pg_tuple = ("Hayden", "point guard", 16.4)
sg_tuple = ("Trey", "shooting guard", 8.2)
sf_tuple = ("Braxon", "small forward", 12.6)
pf_tuple = ("Gunner", "power forward", 14.2)
c_tuple = ("Collin", "center", 6.5)
# Logging the tuples
logger.info(f"Below I have the name, position, and average points per game for each one of your starters:")
logger.info(f"{pg_tuple}")
logger.info(f"{sg_tuple}")
logger.info(f"{sf_tuple}")
logger.info(f"{pf_tuple}")
logger.info(f"{c_tuple}")
# Creating some functions to demonstrate knowledge of tuples
# First name finder - demonstrates knowledge of index positions
def first_name_finder(my_tuple):
    name = my_tuple[0]
    return name
# Running the first name finder
sg_name = first_name_finder(sg_tuple)
logger.info(f"Does the first name finder work? Is your starting shooting guard named {sg_name}?")

# Membership testing
def pf_position_test(another_tuple):
    if another_tuple[1] == "power forward":
        return True
    else:
        return False
# Running the power forward position test
pf_test_fail = pf_position_test(sf_tuple)
logger.info(f"Does Braxon play power forward? {pf_test_fail}")
logger.info(f"Sorry! I will try again!")
pf_test = pf_position_test(pf_tuple)
logger.info(f"Does Gunner play power forwrd? {pf_test}")

# Task 5-5 Creating 2 Sets
# The Sets are list of opponents defeated by two different teams
# Team 1 Set
set_Boston = {"Heat", "Bulls", "Knicks", "Clippers", "Jazz", "Hawks", "Hornets", "Spurs", "Rockets"}
set_Chicago = {"Heat", "Celtics", "Timberwolves", "Grizzlies", "Jazz", "Nuggets", "Spurs"}
# Logging the Sets
logger.info(f"Here is a list of the teams that the Boston Celtics defeated this season: {set_Boston}")
logger.info(f"Here is a list of the teams the Chicago Bulls defeated this season: {set_Chicago}")
# Finding the Unior of the 2 sets
union_set = set_Boston | set_Chicago
# Logging the new set
logger.info(f"Here is a combined list of oppenents that the Boston Celtics and Chicago Bulls defeated: {union_set}")
# Finding the Intersection of the 2 sets
common_set = set_Boston & set_Chicago
logger.info(f"Here is a list of teams that both the Boston Celtics and Chicago Bulls defeated: {common_set}")

with open("text_zen_of_python.txt") as file_object:
        word_list = file_object.read().split()

# Create a dictionary of word counts from a list of words
# A dictionary is always key:value pairs
# Say "I want word:count for each word in word_list"
# Cast the result to a dictionary by using curly braces {}
word_counts_dict2 = {word: word_list.count(word) for word in word_list}

# Logging the information
logger.info("Given text_simple.txt and comprehensions,")
logger.info(f"the the word_counts_dict2 = {word_counts_dict2}")

# Print the logged information
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())

