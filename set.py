
#  Creating Sets
# --------------------
set1 = {1, 2, 3, 4}
set2 = {'apple', 'banana', 'cherry'}
set3 = {1, 2, 3, 3, 2, 1}  # duplicates automatically removed

print("1. Sets Created:")
print("   set1 =", set1)
print("   set2 =", set2)
print("   set3 (duplicates removed) =", set3)

#  Empty set (must use set(), not {})
empty_set = set()
print("   empty_set =", empty_set)

#  From list or tuple
set_from_list = set([10, 20, 30, 20])
print("   set_from_list =", set_from_list)

#  Adding Elements
# -----------------------
fruits = {'apple', 'banana'}
fruits.add('mango')
print("\n2. add() Method:", fruits)

# add() won't add duplicates
fruits.add('apple')
print("   add() ignores duplicates:", fruits)

#  update() - Add multiple elements
# --------------------------------------
fruits.update(['grapes', 'cherry'])
print("\n3. update() Method:", fruits)

# remove() vs discard()
# -----------------------------
nums = {1, 2, 3, 4, 5}
nums.remove(3)
print("\n4. remove():", nums)
# nums.remove(99)  #  KeyError if element not found

nums.discard(99)  #  No error if not found
print("   discard():", nums)

# pop() - Removes random element
# -------------------------------------
colors = {'red', 'green', 'blue', 'yellow'}
popped = colors.pop()
print("\n5. pop(): removed ->", popped)
print("   Remaining set:", colors)

# clear() - Removes all elements
# -------------------------------------
temp = {1, 2, 3}
temp.clear()
print("\n6. clear():", temp)

# copy() - Returns shallow copy
# ------------------------------------
a = {10, 20, 30}
b = a.copy()
b.add(40)
print("\n7. copy():")
print("   Original:", a)
print("   Copy:", b)

# Set Operations (Union, Intersection, Difference, etc.)
# ------------------------------------------------------------
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}

print("\n8. Set Operations:")
print("   Union:", A.union(B))                     # A ∪ B
print("   Intersection:", A.intersection(B))       # A ∩ B
print("   Difference (A-B):", A.difference(B))     # A - B
print("   Symmetric Difference:", A.symmetric_difference(B))  # (A ∪ B) - (A ∩ B)

# Using Operators for Set Operations
# ----------------------------------------
print("\n9. Using Operators:")
print("   A | B =", A | B)   # Union
print("   A & B =", A & B)   # Intersection
print("   A - B =", A - B)   # Difference
print("   A ^ B =", A ^ B)   # Symmetric Difference

# issubset(), issuperset(), isdisjoint()
# --------------------------------------------
X = {1, 2, 3}
Y = {1, 2, 3, 4, 5}
Z = {10, 20}

print("\n10. Relationship Methods:")
print("   X.issubset(Y):", X.issubset(Y))
print("   Y.issuperset(X):", Y.issuperset(X))
print("   X.isdisjoint(Z):", X.isdisjoint(Z))

# len(), max(), min(), sum()
# -----------------------------------
nums = {5, 10, 15, 20}
print("\n11. Built-in Functions:")
print("   len(nums):", len(nums))
print("   max(nums):", max(nums))
print("   min(nums):", min(nums))
print("   sum(nums):", sum(nums))

# Membership Operators
# -----------------------------
print("\n12. Membership Operators:")
print("   10 in nums:", 10 in nums)
print("   25 not in nums:", 25 not in nums)

# Frozenset – Immutable Set
# -----------------------------------
normal_set = {1, 2, 3}
frozen = frozenset(normal_set)
print("\n13. frozenset:")
print("   Frozen set:", frozen)
# frozen.add(4)  #  Error (immutable)

# Iterating through Sets
# -------------------------------
print("\n14. Iterating through a Set:")
animals = {'cat', 'dog', 'lion'}
for a in animals:
    print("   Animal:", a)

# Set Comprehension
# ---------------------------
print("\n15. Set Comprehension:")
squares = {x**2 for x in range(6)}
print("   squares =", squares)

# Convert Between Data Types
# -----------------------------------
print("\n16. Conversion Examples:")
my_list = [1, 2, 2, 3]
converted_set = set(my_list)
print("   List → Set:", converted_set)

my_tuple = tuple(converted_set)
print("   Set → Tuple:", my_tuple)

# Frozen Sets in Dictionary Keys
# ---------------------------------------
frozen_key = frozenset(['name', 'age'])
my_dict = {frozen_key: 'Immutable Key'}
print("\n17. frozenset as dictionary key:", my_dict)

# End of Demo
print("\n All set methods and operations demonstrated successfully!")
