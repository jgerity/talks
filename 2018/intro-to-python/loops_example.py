# Lines beginning with # are comments and will not be executed

i = 0
# Loops as long as the condition of the while loop evaluates to True
# or a value that will be True if converted to a boolean ("Truthy")
print("Begin fizzbuzz while loop")
while i < 100:
    if i % 3 == 0 and i % 5 == 0:  # if the number is divisible by both 3 and 5
      print("Fizzbuzz")
    elif i % 3 == 0:  # if the number is instead only divisible by 3
      print("Fizz")
    elif i % 5 == 0:  # if the number is instead only divisible by 5
      print("Buzz")
    else:  # if none of the above criteria are met, just print the number
      print(i)
    i += 1
print("End while loop\n")
# Notice that the insides of the while loop and if statements are indented! 
# Code blocks in Python are delimited by either tabs or spaces. It's up to 
# you which to use, but the interpreter does require that you be consistent!
# Using 4 spaces for indentation is typical.


# The builtin function range(a, b, [step]) returns an iterable representing the 
# interval [a,b), with an optional (default=1) step size.
# N.B. that in Python2, range() returns a list! range(1000000000) is a lot of 
# values to store all at once, so instead Python 3 prefers to use iterators.

# The `for` keyword takes each element in an iterable and performs some operations
print("Begin for loop")
for x in range(0, 1000):
    print(x, x**2)
print("End for loop\n")

# N.B. that `in` is its own keyword when not associated with a `for`. It is used to
# test whether an object is a member of an iterable.
print(100 in range(100))  # False because range(100) does NOT include 100!

