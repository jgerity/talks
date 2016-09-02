# from __future__ import division
import types


def numbers_ex():
    print(
    """
    # Try these examples in Python 2.x:
    1 + 1
    1 + 5j
    1 + 1.0
    1 / 2
    1. / 2.
    type(1)
    type(1.0)
    type(1j)
    type(1 + 1)
    type(1 + 1.0)
    type(1 + 1j)
    """
    )


def grownup_division():
    print("""
    # Try this piece of magic at the *top* of your Python 2.x script (or uncomment it in this file)
    from __future__ import division

    # Now try:
    1 / 2

    # More information about this magic here: https://www.python.org/dev/peps/pep-0238/
    """)


def list_ex():
    print(
    """
    # Try these examples (check the value of 'a' after each one):
    a = range(0,5)
    a[0]
    a[0] = 5
    a.pop()
    a.insert(0,3)
    a[-1]
    a[0:2]
    a[::2]
    a[1::2]
    [ value * 2 for value in a ]
    sorted(a)
    a.sort()
    a.reverse()
    """
    )


def bool_ex():
   print(
   """
   # Try these examples:
   True
   bool(1)
   bool(0)
   bool("")
   bool("0")
   1 == 1.0
   1 < 2
   [1,2,3] == [1,2,3]
   [1,2,3] is [1,2,3]
   not False
   """
   )


def str_ex():
    print(
    """
    # Try these examples:
    "my string!"
    "Hello" + "World!"
    str(1.0)
    str([1,2,3])
    "LOWER ME".lower()
    "Abc123".isalpha()
    "-".join(["867","5309"])
    """
    )


def dict_ex():
    print(
    """
    # Try these examples (check the value of 'd' after each one):
    d = dict(key1='value1', key2='value2')
    d = {key1: 'value1', key2: 'value2'}
    d['key1']
    d['key1'] = 22 / 7
    d[6] = [1, 1, 2, 3, 5]
    d.keys()
    d.values()
    d.items()
    del d['key2']
    """
    )


print("""
# Try:
numbers_ex()
grownup_division()
list_ex()
bool_ex()
str_ex()
dict_ex()

Curious about an object x?  Try help(x), print((x).__doc__), or dir(x)
""")
