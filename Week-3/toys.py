'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''


# write a function that adds 1
# to the input and prints the result
def inc(a):
    b = a+1
    print(b)


# write a function that adds 1
# to the input and returns the result
def inc_return(d):
    c = d + 1
    return c # hint this is incomplete


# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    return a + b


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    return inc_return(sum(a, b))


# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    if a/2 == int:
        b = True
    return b


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    repeat * phrase
    return

