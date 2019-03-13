"""
Problem 3_5:
Write a function that will look up a phone number given a name.  Use this
dictionary of phone numbers in your program, so that the grader will know
what phone numbers are available.  In it's simplest form, the program will
crash if a name that isn't in its dictionary is asked for.

Here is a printout of one of my runs.

problem3_5("james")
(212) 567-8149

Below is the start of the program including the dictionary.
"""

def problem3_5(name):
    phone_numbers = {"abbie": "(860) 123-4535", "beverly": "(901) 454-3241", \
                     "james": "(212) 567-8149", "thomas": "(795) 342-9145"}

    print(phone_numbers[name])

#print(problem3_5("abbie"))