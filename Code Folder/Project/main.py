'''
Title: Coding with Syntax Project - Multiple Choice Quiz
Name: Jim Finn
Date: 2023/01/06
Requirements: Variables and Operators, Sequence of Statements, Conditional Statements, Iteration, Data Types & Structures, Functions
'''
# Open and import libraries
# Libraries are csv for working with question files, random, os for listing available quizes
import csv
import random
import os

# initialise lists and variables
# List = Question, AnswerA, AnswerB, AnswerC, AnswerD, Answer Key
# Variables: Score, Name, Number of questions needed


'''
Park until rest of game works
# List all files in Question Database Folder
# Ask User for a quiz by either typing in Quiz name or choosing number (Preferred)
# Read in Questions, Answers and Answer Keys and pass to list (Function)
absolutePath = os.path.dirname(__file__) # Solution found @ https://towardsthecloud.com/get-relative-path-python
pathQuestions = "questions"             # also https://pieriantraining.com/iterate-over-files-in-directory-using-python/
fullPath = os.path.join(absolutePath, pathQuestions)
print(fullPath)
print(os.listdir(fullPath))
'''

# Open specific csv file and load into list
file = open("quiz.csv","r")
question = list(csv.reader(file, delimiter=","))
file.close()

print(question)
# Ask for Player name
# Give users a choice between 5, 10, 15 or 20 Questions
# If outside this range display error and ask again.

# Start Game
# Welcome message and instructions

# pick a question at random from the list loaded and display question with all 4 options


# Ask for user input by choosing A to D


# check answer against answer key
# if not an accepted answer A to D ask again (Error Message)
    # If correct add 10 to score
    # if Incorrect subtract 5 from score

# Check if you have asked all questions
# if yes then end quiz otherwise ask another one

# end quiz (Function)
# display final score and proportion of right and wrong questions