#  Creating Tuples
# -----------------------
t1 = (1, 2, 3, 4)
t2 = ('apple', 'banana', 'cherry')
t3 = (1, 2, 'three', True, 3.5)

print("1. Tuples Created:")
print("   t1 =", t1)
print("   t2 =", t2)
print("   t3 =", t3)

#  Single element tuple – must have a comma
single = (5,)
print("\n   Single element tuple:", single)

#  Without parentheses
t4 = 10, 20, 30
print("   Tuple without parentheses:", t4)

#  Nested tuple
nested = (1, (2, 3), (4, 5))
print("   Nested tuple:", nested)

#  Tuple from iterable
t_from_list = tuple([10, 20, 30])
print("   Tuple from list:", t_from_list)

#  Empty tuple
empty = ()
print("   Empty tuple:", empty)

# Accessing Elements
# -------------------------
t = ('a', 'b', 'c', 'd', 'e')
print("\n2. Accessing Elements:")
print("   t[0] =", t[0])     # First element
print("   t[-1] =", t[-1])   # Last element
print("   Slicing t[1:4] =", t[1:4])

# Tuple is Immutable
# -------------------------
print("\n3. Immutability Example:")
immutable_tuple = (1, 2, 3)
try:
    immutable_tuple[1] = 99   #  Not allowed
except TypeError as e:
    print("   Error:", e)

# count() Method
# -------------------------
numbers = (1, 2, 2, 3, 2, 4)
print("\n4. count() Method:")
print("   Count of 2:", numbers.count(2))

# index() Method
# -------------------------
letters = ('a', 'b', 'c', 'b')
print("\n5. index() Method:")
print("   Index of 'b':", letters.index('b'))
print("   Index of 'c':", letters.index('c'))

# len(), max(), min(), sum()
# ---------------------------------
nums = (10, 20, 5, 15)
print("\n6. Built-in Functions:")
print("   Length:", len(nums))
print("   Max:", max(nums))
print("   Min:", min(nums))
print("   Sum:", sum(nums))

# Membership Operators
# ---------------------------
print("\n7. Membership Operators:")
print("   10 in nums:", 10 in nums)
print("   100 not in nums:", 100 not in nums)

# Tuple Concatenation (+) and Repetition (*)
# ------------------------------------------------
a = (1, 2)
b = (3, 4)
print("\n8. Concatenation and Repetition:")
print("   a + b =", a + b)
print("   a * 3 =", a * 3)

# Tuple Unpacking
# ----------------------
person = ('Kamil', 25, 'Web Developer')
name, age, job = person
print("\n9. Tuple Unpacking:")
print("   Name:", name)
print("   Age:", age)
print("   Job:", job)

# Using * (star) for variable-length unpacking
data = (1, 2, 3, 4, 5)
a, *middle, b = data
print("   a =", a)
print("   middle =", middle)
print("   b =", b)

# Nested Tuples and Access
# ------------------------------
nested = (('Python', 'Java'), ('HTML', 'CSS'))
print("\n10. Nested Tuple Access:")
print("   nested[0][1] =", nested[0][1])

# Tuple in Loops
# ------------------------
print("\n11. Looping Through Tuple:")
colors = ('red', 'green', 'blue')
for color in colors:
    print("   Color:", color)

# Converting Between Tuples and Lists
# --------------------------------------------
print("\n12. Tuple ↔ List Conversion:")
tup = (1, 2, 3)
lst = list(tup)
lst.append(4)
print("   Converted to list:", lst)
tup2 = tuple(lst)
print("   Back to tuple:", tup2)

#  Nested Tuple Iteration
# -------------------------------
print("\n13. Nested Tuple Iteration:")
nested = ((1, 2), (3, 4), (5, 6))
for x, y in nested:
    print(f"   Pair: {x}, {y}")

#  Tuple as Dictionary Key (Immutable)
# --------------------------------------------
print("\n14. Tuple as Dictionary Key:")
location = {}
key = (24.8607, 67.0011)
location[key] = "Karachi"
print("   Dictionary with tuple key:", location)

#  Built-in Functions for Tuples
# -------------------------------------
nums = (10, 20, 30, 40)
print("\n15. Built-in Functions:")
print("   all(nums):", all(nums))     # True (all non-zero)
print("   any(nums):", any(nums))     # True (any non-zero)
print("   sorted(nums):", sorted(nums))
print("   reversed(nums):", tuple(reversed(nums)))

# End of Demo
print("\n All tuple operations demonstrated successfully!")
