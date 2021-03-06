#!/usr/bin/env python

i = 0
# Loops as long as the condition of the while loop evaluates to True
# (or a value that will be True if converted to a boolean)
while i < 10:
    print(i)
    i += 1

# Notice that the inside of the while loop is indented!

# range(a,b) returns the integer range [a,b), which we then assign
# to the variable 'numbers'
numbers = range(0,10)

# 'for' behaves a little differently, taking each element of an 'iterable'
# object ('numbers' in this case) and performing a set of operations on it.
for x in numbers:
    print(x)
