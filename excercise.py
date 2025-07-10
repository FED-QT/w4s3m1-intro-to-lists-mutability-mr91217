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

# ===

# Part 2: Lists & Loops
names = ["alice", "bob", "charlie", "dana"]

# Task A: build upper_names
upper_names = []
for n in names:
    # TODO: append uppercase n
    pass

# Task B: enumerate over upper_names
# for :
    # TODO: print index and name
#    pass

# Task C: demo two list methods
# 1. insert
# TODO
# 2. remove
# TODO
# 3. sort
# TODO
