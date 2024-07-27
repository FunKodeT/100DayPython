#################################################################
# PROGRAM: STUDENT GRADING SYSTEM
#----------------------------------------------------------------

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
    student_grades[key] = [student_scores[key]]
    var = student_scores.get(key)
    var = int(var)
    if var >= 91:
        student_grades[key] = 'Outstanding!'
    elif var >= 81:
        student_grades[key] = 'Exceeds Expectations!'
    elif var >= 71:
        student_grades[key] = 'Acceptable.'
    else:
        student_grades[key] = 'Failure!'

print(student_grades)

# {'Harry': 'Exceeds Expectations!', 'Ron': 'Acceptable.', 'Hermione': 'Outstanding!', 'Draco': 'Acceptable.', 'Neville': 'Failure!'}

#----------------------------------------------------------------
#################################################################
#----------------------------------------------------------------
PROGRAM1_V2 = {
#----------------------------------------------------------------
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.

# student_grades = {}

# # TODO-2: Write your code below to add the grades to student_grades.👇

# for key in student_scores:
#     student_grades[key] = [student_scores[key]]
#     var = student_scores.get(key)
#     var = int(var)
#     if var >= 91:
#         student_grades[key] = 'Outstanding!'
#     elif var >= 81:
#         student_grades[key] = 'Exceeds Expectations!'
#     elif var >= 71:
#         student_grades[key] = 'Acceptable.'
#     else:
#         student_grades[key] = 'Failure!'

# # 🚨 Don't change the code below 👇
# print(student_grades)

# # {'Harry': 'Exceeds Expectations!', 'Ron': 'Acceptable.', 'Hermione': 'Outstanding!', 'Draco': 'Acceptable.', 'Neville': 'Failure!'}

}
#----------------------------------------------------------------
PROGRAM1_V1 = {
#----------------------------------------------------------------
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.

# student_grades = {}

# # TODO-2: Write your code below to add the grades to student_grades.👇

# for key in student_scores:
#     student_grades[student_scores] = student_scores[key]

# # 🚨 Don't change the code below 👇
# print(student_grades)

# # ERROR

}
#----------------------------------------------------------------
PROGRAM1_V0 = {
#----------------------------------------------------------------
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.

# student_grades = {}

# # TODO-2: Write your code below to add the grades to student_grades.👇

# for key in student_scores:
#     student_grades[[key]] = student_scores[key]

# # 🚨 Don't change the code below 👇
# print(student_grades)

# # ERROR

}
# ----------------------------------------------------------------
INSTRUCTIONS1_V0 = {
#----------------------------------------------------------------
# Instructions
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.

# The final version of the student_grades dictionary will be checked.

# DO NOT modify lines 1-7 to change the existing student_scores dictionary.

# DO NOT write any print statements.

# This is the scoring criteria:

# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"

# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
# Hint
# Remember that looping through a Dictionary will only give you the keys and not the values.

# If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values.

# At the end of your program, the print statement will show the final student_scores dictionary, do not change this.

}
#----------------------------------------------------------------
#################################################################
#----------------------------------------------------------------
TEST3_V0 = {
#----------------------------------------------------------------
## CREATE AN EMPTY DICTIONARY
# empty_dictionary = {}
# empty_dictionary['New'] = 'Example'

## print(empty_dictionary)

## {'New': 'Example'}

}
#----------------------------------------------------------------
#################################################################
#----------------------------------------------------------------
TEST2_V0 = {
#----------------------------------------------------------------
# list = ['a', 'b', 'c']
# print(list[4])

## ERROR

}
#----------------------------------------------------------------
#################################################################
#----------------------------------------------------------------
TEST1_V7 = {
#----------------------------------------------------------------
# programming_dictionary = {
#     'print()': 'Python version of console.log.',
#     'input()': 'Allows input that becomes the value of input. If assigned to a variable, will save the value to that variable.',
#     'str()': 'Python version of String().',
#     'list[0]': 'Python version of array().',
#     'Bug': 'An error in a program that prevents the program from running as expected.',
#     'Function': 'A piece of code that you can easily call over and over again.',
# }

# programming_dictionary['Loop'] = 'The action of doing something over and over again.'

# programming_dictionary['Bug'] = 'A moth in your computer.'

# # LOOP THROUGH A DICTIONARY
# for key in programming_dictionary: 
#     print(key)
#     print(programming_dictionary[key])

# # print(); Python version of console.log.; input(); Allows input that becomes the value of input. If assigned to a variable, will save the value to that variable.; str(); Python version of String().; list[0]; Python version of array().; Bug; A moth in your computer.; Function; A piece of code that you can easily call over and over again.; Loop; The action of doing something over and over again.

}
#----------------------------------------------------------------
TEST1_V6 = {
#----------------------------------------------------------------
# programming_dictionary = {
#     'print()': 'Python version of console.log.',
#     'input()': 'Allows input that becomes the value of input. If assigned to a variable, will save the value to that variable.',
#     'str()': 'Python version of String().',
#     'list[0]': 'Python version of array().',
#     'Bug': 'An error in a program that prevents the program from running as expected.',
#     'Function': 'A piece of code that you can easily call over and over again.',
# }

# programming_dictionary['Loop'] = 'The action of doing something over and over again.'

# programming_dictionary['Bug'] = 'A moth in your computer.'

# # LOOP THROUGH A DICTIONARY
# for thing in programming_dictionary: print(thing)

# # print(); input(); str(); list[0]; Bug; Function;

}
#----------------------------------------------------------------
TEST1_V5 = {
#----------------------------------------------------------------
# programming_dictionary = {
#     'print()': 'Python version of console.log.',
#     'input()': 'Allows input that becomes the value of input. If assigned to a variable, will save the value to that variable.',
#     'str()': 'Python version of String().',
#     'list[0]': 'Python version of array().',
#     'Bug': 'An error in a program that prevents the program from running as expected.',
#     'Function': 'A piece of code that you can easily call over and over again.',
# }

## EDIT AN ITEM IN AN EXISTING DICTIONARY
# programming_dictionary['Bug'] = 'A moth in your computer'
# print(programming_dictionary['Bug'])

## A moth in your computer

}
#----------------------------------------------------------------
TEST1_V4 = {
#----------------------------------------------------------------
# programming_dictionary = {
#     'print()': 'Python version of console.log.',
#     'input()': 'Allows input that becomes the value of input. If assigned to a variable, will save the value to that variable.',
#     'str()': 'Python version of String().',
#     'list[0]': 'Python version of array().',
#     'Bug': 'An error in a program that prevents the program from running as expected.',
#     'Function': 'A piece of code that you can easily call over and over again.',
# }

## WIPE AN EXISTING DICTIONARY
# programming_dictionary = {}
# print(programming_dictionary)

## {}

}
#----------------------------------------------------------------
TEST1_V3 = {
#----------------------------------------------------------------
# programming_dictionary = {
#     'print()': 'Python version of console.log.',
#     'input()': 'Allows input that becomes the value of input. If assigned to a variable, will save the value to that variable.',
#     'str()': 'Python version of String().',
#     'list[0]': 'Python version of array().',
#     'Bug': 'An error in a program that prevents the program from running as expected.',
#     'Function': 'A piece of code that you can easily call over and over again.',
# }

## RETRIEVING ITEMS FROM DICTIONARY
# print(programming_dictionary['Function'])

## A piece of code that you can easily call over and over again.

## ADDING NEW ITEMS TO DICTIONARY
# programming_dictionary['Loop'] = 'The action of doing something over and over again.'

# print(programming_dictionary)

## {'print()': 'Python version of console.log.', 'input()': 'Allows input that becomes the value of input. If assigned to a variable, will save the value to that variable.', 'str()': 'Python version of String().', 'list[0]': 'Python version of array().', 'Bug': 'An error in a program that prevents the program from running as expected.', 'Function': 'A piece of code that you can easily call over and over again.', 'Loop': 'The action of doing something over and over again.'}

}
#----------------------------------------------------------------
TEST1_V2 = {
#----------------------------------------------------------------
## PYTHON DICTIONARIES ARE BASICALLY .JSON FORMAT
# programming_dictionary = {
#     'print()': 'Python version of console.log.',
#     'input()': 'Allows input that becomes the value of input. If assigned to a variable, will save the value to that variable.',
#     'str()': 'Python version of String().',
#     'list[]': 'Python version of array().',
#     'Bug': 'An error in a program that prevents the program from running as expected.',
#     'Function': 'A piece of code that you can easily call over and over again.',
#     'Loop': 'The action of doing something over and over again.'
# }

# print(programming_dictionary[Function])

## ERROR

}
#----------------------------------------------------------------
TEST1_V1 = {
#----------------------------------------------------------------
## PYTHON DICTIONARIES ARE BASICALLY .JSON FORMAT
# programming_dictionary = {
#     'print()': 'Python version of console.log.',
#     'input()': 'Allows input that becomes the value of input. If assigned to a variable, will save the value to that variable.',
#     'str()': 'Python version of String().',
#     'list[0]': 'Python version of array().',
#     'Bug': 'An error in a program that prevents the program from running as expected.',
#     'Function': 'A piece of code that you can easily call over and over again.',
#     'Loop': 'The action of doing something over and over again.'
# }

# print(programming_dictionary['Bog'])

## ERROR

}
#----------------------------------------------------------------
TEST1_V0 = {
#----------------------------------------------------------------
## PYTHON DICTIONARIES ARE BASICALLY .JSON FORMAT

# programming_dictionary = {
#     'print()': 'Python version of console.log.',
#     'input()': 'Allows input that becomes the value of input. If assigned to a variable, will save the value to that variable.',
#     'str()': 'Python version of String().',
#     'list[0]': 'Python version of array().',
#     'Bug': 'An error in a program that prevents the program from running as expected.',
#     'Function': 'A piece of code that you can easily call over and over again.',
#     'Loop': 'The action of doing something over and over again.'
# }

# print(programming_dictionary['Bug'])

## An error in a program that prevents the program from running as expected.

}
#----------------------------------------------------------------
#################################################################
