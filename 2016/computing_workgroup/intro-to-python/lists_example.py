#!/usr/bin/env python


arr = [1, 2, 3]
print(len(arr))  # Here, we use the `len` function to find the list's length
print(arr[0])  # lists are indexed from zero

# We can reassign one of the slots in arr
arr[1] = 10

# And we can add to the end of the array with the append() method
# Notice that nowhere on this line do we actually use = to assign!
arr.append(4)
print(arr)

# We can also add an element anywhere we'd like with the insert() method
# Let's put a string in the second slot, lists don't have to have the same
# type of object in every slot, like arrays in some languages.
arr.insert(1, "Move over!")

print(arr)

# We can even put another list in one of the slots
arr.append(["a", "new", "list"])
print(arr)

# If we have a list of things we want to add, we can extend() the list all
# at once instead of insert()ing or append()ing them one at a time
arr.extend([0, 0, 0])
print(arr)

# We can pop() the last entry off the end of the list
element = arr.pop()

print(arr)
print(element)

# In fact, we can pop() any entry we want if we ask for a specific index!
element = arr.pop(0)
print(arr)
print(element)
