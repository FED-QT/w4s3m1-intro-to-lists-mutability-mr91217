# exercise.py
# Part 1: Mutable vs Immutable
a = 100
b = a
print("Before:", a, b, id(a), id(b))

a += 1
print("After a += 1:", a, b, id(a), id(b))

x = [1, 2, 3]
y = x
print("Before:", x, y, id(x), id(y))

x.append(4)
print("After x.append(4):", x, y, id(x), id(y))

# * Why did `id(a)` change but `id(x)` did not?
#     Because a is an integer which is immutable, changing its value creates a new object.x is a list which is mutable, so it is modified.
# * What does this say about integers vs. lists in Python?
#     Integers are immutable, lists are mutable.

# ===

# Part 2: Lists & Loops
names = ["alice", "bob", "charlie", "dana"]

# Task A: build upper_names
upper_names = []
for n in names:
    # TODO: append uppercase n
    upper_names.append(n.capitalize())

# Task B: enumerate over upper_names
for idx, name in enumerate(upper_names, start=1):
    # TODO: print index and name
#    pass
    print(f"{idx}. {name}")

# Task C: demo two list methods
# 1. insert
# TODO
upper_names.insert(2, "Tofu")
print("Insert:", upper_names)
# 2. remove
# TODO
upper_names.remove("Charlie")
print("Remove:", upper_names)
# 3. sort
# TODO
upper_names.sort()
print("Sort:", upper_names)


#  * **Compare**: What patterns did you notice about mutability?
# Mutable keep the same id after modified, and Immutable get a new id after modified.
#  * **Reflect**: When might you prefer immutability? When is a list’s mutability useful?
# When you need data that shouldn’t be changed—like constants, dictionary keys.
# When you want to edit items without making a whole new list.