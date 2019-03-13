
#%%
def problem1_5(age):

    """
    Problem 1_5:
    Write a function 'problem1_5(age)'. This function should use if-elif-else
    statement to print out "Have a glass of milk." for anyone under 7; "Have
    a coke." for anyone under 21, and "Have a martini." for anyone 21 or older.

    Tip: Be careful about the ages 7 (a seven year old is not under 7) and 21.
    Also be careful to make the phrases exactly as shown for the auto-grader.
    """
    if age < 7:
        print("Have a glass of milk.")
    elif age < 21: #and age >= 7:
        print("Have a coke.")
    else:
        print("Have a martini.")

#print(problem1_5(25))
