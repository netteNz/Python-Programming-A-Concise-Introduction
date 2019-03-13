"""
Problem 3_3:
Write a function that will convert a date from one format to another.
Specifically, 06/10/2016 should convert to June 17, 2016.  Actually, you
will input the 6, the 17, and the 2016 as separate integers (numbers) and
the function will assemble and print the date as June 17, 2016.  I suggest
that you create a tuple months = ("January", "February", "March", ...) to
store the names of the months.  Then it is easy to access the name February
as months[1] and so on.

Here is printout of my run.
problem3_3(6,17,2016)
June 17, 2016

*** Note: for simplicity use 6 and not 06 for numbers; otherwise, the
function will confuse Python and will have to be more complex to work. ***
*** Tip: In print statements, commas create a space.  So you may have difficulty
avoiding a space between the 17 above and the following comma.  I suggest
that you build the output as a single string containing the properly formatted
date and then print that.  You can convert any number to string by using str()
and tie the parts together using +. Duplicate the format of the example output
exactly. Everything you need to do this is covered in the lectures. ***
"""

def problem3_3(month, day, year):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']

    print(str(months[month-1])+' '+ str(day)+', '+str(year))

#print(problem3_3(6,17,2016))
