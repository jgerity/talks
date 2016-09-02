import time

"""
These scripts are designed to be run semi-interactively (try invoking with `python -i script.py`)
Any line marked ### is a good example to try!
"""

# notice that some of this function's arguments have default values
def count(stop, start=0, how_long=False):
   """
   Print all integers between two values, inclusive.
   start=0 - beginning value
   stop=1e6 - ending value
   how_long - if True, prints how long the process took
   """
   t = time.clock()
   i = start
   while i < stop:
       print(i)
       i += 1

   if how_long:
       print("Process took %s seconds" % str(time.clock() - t))

# notice that we can refer to arguments by their name, and in any order!
### count(10)
### count(10, -2)
### count(start=-3, stop=3)
### count(20, how_long=True)


def yell(*args, **kwargs):
    # *args is a special way to allow for a variable number of arguments
    # this can be done with keyword arguments, too (* unpacks a tuple, ** a dictionary).
    # often in Python, you'll see functions with the signature: func(*args, **kwargs)
    # further reading: https://docs.python.org/2/tutorial/controlflow.html#arbitrary-argument-lists
    for thing in args:
        print( str(thing).upper() )

    for key in kwargs.keys():
        print("I was given the keyword %s with value %s" % (key, kwargs[key]))

### yell("hi there!")
### yell("the old grey mule she", "ain't what she used to be", "ain't what she used to be", "ain't what she used to be")

# *args will be an empty tuple in this case, but that won't break our function!
### yell(firstarg=[1,2,3], secondarg="spaghetti")
