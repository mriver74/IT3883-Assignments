# Program Name: Assignment2.py
# Course: IT3883/Section 01
# Student Name: Jack Rivers
# Assignment Number: Lab#2
# Due Date: 10/02/2026
# Purpose: The program takes the input file, reads it, and splits it up into lists. These lists are then sorted
# into an average score and name. These variables are sorted into one big listed which displays each students'
# name and average score in descending order.
# No specific resources used, other than Python functions.

# set variables
students = []

# read file. extract names and scores
with open("/Users/jackrivers/Downloads/Assignment2input.txt", "r") as file:
    for line in file:
        x = line.split()
        # set name and scores as variables from each list
        name = x[0]
        og_scores = [float(y) for y in x[1:]]
        # average score and append to student list
        average_score = sum(og_scores)/len(og_scores)
        students.append((name, average_score))

# sort by desc. average and print results to hundredth place
students.sort(key=lambda student: student[1], reverse=True)
for name, average_score in students:
    print(f"{name} {average_score:.2f}")
