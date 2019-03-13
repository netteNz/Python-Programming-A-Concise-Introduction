"""
Problem 1_6:
Write a function 'problem1_6()' that prints the odd numbers from 1 through 100.
Make all of these numbers appear on the same line (actually, when the line
fills up it will wrap around, but ignore that.). In order to do this, your
print statement should have end=" " in it. For example, print(name,end=" ")
will keep the next print statement from starting a new line. Be sure there is a
space between these quotes or your numbers will run together. Use a single
space as that is what the grading program expects. Use a 'for' loop
and a range() function.

Things to be careful of that might go wrong: You print too many numbers, you
put too much or too little space between them, you print each number on its
own line, you print even numbers or all numbers, your first number isn't 1 or
your last number isn't 99.  Always check first and last outputs when you write
a loop.
"""

def problem1_6():
    for n in range(1, 100):
        if n % 2 != 0:
            print(str(n)+" ", end='')

#print(problem1_6())