"""
Problem 3_2:
Below you see three objects which are of collection data type: a list, a tuple,
and a string. Although different in many ways, you can write a 'for' loop that
steps through a "collection" and it will work with all three. This problem
is started for you. Finish it by writing the loop that will step through the
collection and print out its items, one per line. Test it and make sure that
it works for all three of the following data objects.

Be sure that your code does not include the name of any one of these data
collections. That would stop it from being general enough to deal with a
different collection.  The grader will use different data.

There is a printout of my run after the problem starter.
"""

#nlis = [23,64,23,46,12,24]          # list
#atup = ("c","e","a","d","b")        # tuple
#str1 = "Rumplestilskin"             # string

def problem3_2(collection):

    for item in collection:
        print(str(item)+'\n', end='')

#print(problem3_2(atup))