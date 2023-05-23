"""
Author: Wade Bryson

Purpose: Analyze a basketball team's point differentials for a full season.

"""

# import some standard modules first - how many can you make use of?
# Imported needed modules
import math
import statistics

# TODO: import from local util_datafun_logger.py 
# Setting up logger
from util_datafun_logger import setup_logger

# Calling the logger
logger, logname = setup_logger(__file__)

# Created a list based on the point differentials for a basketball teams full season.
list1 = [4, 8, -12, 20, 12, 3, -5, -7, 21, -5, -23, 32, 27, 10, 5, 4, 7, 8, -10, 17]
logger.info(f"Your list of point differentials = " + str(list1))

# Created two lists that track our teams goals of making 1,000 Free Throws in the next 10 days.
# This list contains each Day throughout our 10 Day Challenge.
listx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# This list contains the total amount of FTs made by our team after each day.
listy = [100, 200, 295, 405, 500, 620, 680, 800, 910, 1050]
logger.info(f"Below is your data about your 10 Day Free Throw Challenge.")
logger.info(f"Days:{listx}")
logger.info(f"Total Free Throws Made:{listy}")

# Task 3 Lists 1 - List Statistics
# Calculating measures of central tendency
mean = statistics.mean(list1)
median = statistics.median(list1)
mode = statistics.mode(list1)
# Logging this information
logger.info(f"Let's look at some basic statistics regarding your point differentials list!")
logger.info(f"mean   = {mean:.2f}")  
logger.info(f"median = {median:.2f}")
logger.info(f"mode   = {mode:.2f}")
# Calculating the standard deviation and variance
var = statistics.variance(list1)
stdev = statistics.stdev(list1)
# Change to f-strings and use 2 decimal places
logger.info(f"var    = {var:.2f}")
logger.info(f"stdev  = {stdev:.2f}")

# Task 3 Lists 2 - Correlation and Prediction
# Calculate and log the correlation
xy_corr = statistics.correlation(listx, listy)
logger.info(f"Let's explore the relationship created from your 10 Day Free Throw Challenge")
logger.info(f"The correlation between your Days and Total Free Throws Made = {xy_corr:.2f}")
# Calculate Slope and y-intercept of the line of best fit
slope, intercept = statistics.linear_regression(listx, listy)
logger.info(f"The slope for your line of best fit = {slope:.2f}")
logger.info(f"The y-intercept for your line of best fit = {intercept:.2f}")
logger.info(f"The equation for your line of best fit is y = {slope:.2f}x +{ intercept:.2f}")
#Using the line of best fit to predict a value
future_time = 15
future_y = round(slope * future_time + intercept)
logger.info(f"If you keep up the Free Throw Challenge for 5 more days I predict you will have made a total of {future_y:.2f} free throws!")

# Task 3 Lists 3 - Using Python Built-in Functions
# Calculating Lowest Value
lowest = min(list1)
logger.info(f"Your worst point differential was {lowest}.")
# Calculating Highest Value
highest = max(list1)
logger.info(f"Your best point differential was {highest}.")
# Calculating Length
length = len(list1)
logger.info(f"You played a total of {length} games this season.")
# Calculating Sum
total = sum(list1)
logger.info(f"Your total point differential for the season was {total}.")
# Calculating Average
# Question - Is there a difference between using the statistics.mean and doing it the way I did below? They look the same to me but I'm new to all of this.
average = total / length
logger.info(f"Your average point differential was {average}.")
# Creating a set of list1. This will remove any duplicates.
set1 = set(list1)
logger.info(f"In this new set I removed all the duplicated point differentials {set1}.")
# Creating a sorted list
asc_list1 = sorted(list1)
logger.info(f"Your list sorted from your worst point differentials to your best is {asc_list1}.")
# Creating a reverse sorted list
des_list1 = sorted(list1, reverse=True)
logger.info(f"Your list sorted from your best point differntials to your worst is {des_list1}.")

# Task 3 Lists 4 - List Methods
# Creating some short lists that feature the amount of 3-pointers made in a game
lst = [2, 3, 5, 1, 9, 2, 7, 8, 4]
lst2 = [3, 4, 8, 1, 7]
logger.info(f"Your list of 3-pointers made = {lst}")
# Append a single value
lst.append(6)
logger.info(f"Your new list of 3-pointers made = {lst}")
# Extend lst by adding lst2 to it
lst.extend(lst2)
logger.info(f"Your combined list of 3-pointers made = {lst}")
# Insert an item into lst
lst.insert(1, 9)
logger.info(f"After your addition, your new list of 3-pointers made = {lst}")
# Removing the number 5 from lst
lst.remove(5)
logger.info(f"After removing the number 5, your new list of 3-pointers made = {lst}")
# Counting the number of 2s in the list
numb2 = lst.count(2)
logger.info(f"You made 2 threes {numb2} times this season")
# Sorting your list in ascending order
lst.sort()
logger.info(f"Here is your list sorted in numerical order = {lst}")
# Sorting your list in descending order
lst.sort(reverse=True)
logger.info(f"Here is your list sorted in descending numerical order = {lst}")
# Creating a copy of the lst list
new_list = lst.copy()
logger.info(f"Here is a copy of your list of 3-pointers made = {new_list}")
# Modify your new list by removing the first and last value
new_list.pop(0)
new_list.pop()
logger.info(f"Here is your new list after removing the first and last values = {new_list}")

# Task 3 Lists 5 - List Transformations
# Using the filter function to filter out point differentials for games we lost
# Create a function to determine games that you won (Point differentials > 0)
def win_loss(point_differential):
    if point_differential > 0:
        return True
    else:
        return False
# Using the filter function
filtered = filter(win_loss, list1)
logger.info(f"The point differentials for the games you won are listed below")
for p in filtered:
    logger.info(f"{p}")
# Defining the cube root function
def cube_root(x):
    cube_root = math.cbrt(x)
    nice_number = round(cube_root, 2)
    return(nice_number)
# Using the map function to cube root my 3-pointers made list
# I am using this list because the values are all positive. You could edit the cube root function to account for negatives, but I did not.
mapcbr3 = map(cube_root, lst)
logger.info(f"Here are the cube root values of your 3-pointers made list {mapcbr3}")

# Using the map function to find the volume of a cube given the side length found in the list mapcbr3
# Note - Because I rounded to two decimal places this new list will not equal the original list
# Defining Volume of a Cube Function
def volume(X):
    volume = X*X*X
    nice_volume = round(volume, 2)
    return(nice_volume)
#Using the map function find the volume of a cube with the given lengths from list lst
mapvolume = map(volume, mapcbr3)
logger.info(f"Here are the volumes of a cube given the side lenght in the list above {mapvolume}")

# Task 3 Lists 6 - Using List Comprehension
# Using List Comprehension to create a new list showing just the games lost
games_lost = [x for x in list1 if x < 0]
logger.info(f"Here are the games you lost {games_lost}.")
# Using List Comprehension to triple each value
games_lost_x3 = list(map(lambda t: t*3, games_lost))
logger.info(f"Here are your games lost point differentials if everything was tripled = {games_lost_x3}")
# Using List Comprehension to do whatever you want. I want to add 25 points to each value.
games_lost_add_headstart = list(map(lambda k: k+25, games_lost))
logger.info(f"Here are your games lost point differentials if you would have started with a 25 points head start = {games_lost_add_headstart}")
logger.info(f"You could have went UNDEFEATED if you would have received that head start........")

# Print the logged information
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())



