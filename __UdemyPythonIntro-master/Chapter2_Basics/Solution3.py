"""Exercise 2:
1.)
Write a function that takes a dictionary as an input.
The function then iterates over all values of each key and counts how many
Students are in the dictionary. (See d below)
2.)
Write a function that iterates over all key, value pairs of the dictionary and
prints the name of the student.
"""


def exercise1(dct):
    num_students = 0
    for val in dct.values():
        if val == "Student":
            num_students += 1
    return num_students


def exercise2(dct):
    for key, val in dct.items():
        if val == "Student":
            print(key, "is a student")


d = {"Oskar": "Student", "Jan": "Instructor", "Thomas": "Student"}
print(exercise1(d))

exercise2(d)
