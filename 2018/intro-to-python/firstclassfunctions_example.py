#!/usr/bin/env python

def makeAddFunction(x):
    """
    This function represents breaking the operation x+y into two steps, by
    returning a function F(y) that "knows" what value of x to use.  In more
    specific terms, the value of x is stored in the "closure" of the function
    that is created.
    """
    def newFunc(y):
        """ This function 'carries' knowledge about x with it """
        return x+y

    # Having defined newFunc, let's spit it out to whoever wants it
    # Notice that we are *not* calling newFunc with parentheses
    return newFunc


addOne = makeAddFunction(1)
addTwo = makeAddFunction(2)

print(addOne(1))  # 1 + 1 = 2
print(addOne(2))  # 1 + 2 = 3
print(addTwo(1))  # 2 + 1 = 3
print(addTwo(2))  # 2 + 2 = 4


def addManyTimes(addFunc):
    """
    We can even pass functions as arguments to other functions.  This function
    calls the given function with the arguments [0,1,...,10]
    """
    for num in range(0, 11):
        print("addManyTimes: Adding %i, result is %i" % (num, addFunc(num)))

addManyTimes(addOne)  # Notice that we're not calling addOne here, either
addManyTimes(addTwo)


# Python has a special type of function called a lambda that allows us to
# define a short function in-line

addManyTimes(lambda y: 3+y)

# Here, the lambda expression is a function that takes one argument (y) and
# returns the result of 3+y.  This lambda is equivalent to makeAddFunction(3)
