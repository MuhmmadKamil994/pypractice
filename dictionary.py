#Creating Dictionaries
# ---------------------------
person = {
    "name": "Kamil",
    "age": 25,
    "job": "Web Developer"
}

empty_dict = {}
dict_from_list = dict([("a", 1), ("b", 2)])
dict_from_keys = dict.fromkeys(["x", "y", "z"], 0)

print("1. Dictionaries Created:")
print("   person =", person)
print("   empty_dict =", empty_dict)
print("   dict_from_list =", dict_from_list)
print("   dict_from_keys =", dict_from_keys)

#  Accessing Values
# -----------------------
print("\n2. Accessing Values:")
print("   person['name'] =", person["name"])
print("   person.get('age') =", person.get("age"))
print("   person.get('salary', 'Not Available') =", person.get("salary", "Not Available"))

#  Adding or Updating Elements
# ----------------------------------
person["salary"] = 50000       # Add
person["age"] = 26             # Update
print("\n3. Adding / Updating Elements:", person)

#  remove() vs pop() vs popitem()
# -------------------------------------
data = {"a": 1, "b": 2, "c": 3}
data.pop("b")       # Removes key 'b'
print("\n4. pop():", data)

data.popitem()      # Removes last inserted item
print("   popitem():", data)

# del statement
del data["a"]
print("   del:", data)

#  keys(), values(), items()
# -------------------------------
person = {"name": "Kamil", "age": 26, "job": "Web Developer"}
print("\n5. keys():", list(person.keys()))
print("   values():", list(person.values()))
print("   items():", list(person.items()))

#  clear() - Remove all items
# ---------------------------------
temp = {"x": 1, "y": 2}
temp.clear()
print("\n6. clear():", temp)

#  copy() - Shallow copy
# -----------------------------
original = {"a": 1, "b": 2}
copy_dict = original.copy()
copy_dict["c"] = 3
print("\n7. copy():")
print("   Original:", original)
print("   Copy:", copy_dict)

#  setdefault() - Add key if not present
# ---------------------------------------------
person.setdefault("country", "Pakistan")
person.setdefault("age", 30)  # Will not update existing
print("\n8. setdefault():", person)

#  update() - Merge dictionaries
# ------------------------------------
extra = {"salary": 50000, "city": "Karachi"}
person.update(extra)
print("\n9. update():", person)

#  Dictionary Comprehension
# -------------------------------
squared = {x: x**2 for x in range(5)}
print("\n10. Dictionary Comprehension:", squared)

# Membership Operators
# -------------------------------
print("\n11. Membership Operators:")
print("   'name' in person:", 'name' in person)
print("   'gender' not in person:", 'gender' not in person)

#  Iterating Dictionaries
# --------------------------------
print("\n12. Iterating through dictionary:")
for key in person:
    print("   Key:", key, "Value:", person[key])

# Using items()
for key, value in person.items():
    print("   Key:", key, "Value:", value)

#  Nested Dictionaries
# ------------------------------
company = {
    "employee1": {"name": "Kamil", "age": 26},
    "employee2": {"name": "Ali", "age": 30}
}
print("\n13. Nested Dictionary:")
print("   employee1 name:", company["employee1"]["name"])

# Dictionary with different data types
# -----------------------------------------------
mixed_dict = {
    1: "integer key",
    3.14: "float key",
    (1, 2): "tuple key"
}
print("\n14. Dictionary with different key types:", mixed_dict)

#  Built-in Functions on Dictionaries
# --------------------------------------------
nums = {"a": 10, "b": 20, "c": 30}
print("\n15. Built-in Functions:")
print("   len(nums):", len(nums))
print("   max(nums):", max(nums))  # max key
print("   min(nums):", min(nums))  # min key
print("   sum(nums.values()):", sum(nums.values()))

#  Converting Between Data Types
# ---------------------------------------
keys = ["x", "y", "z"]
values = [1, 2, 3]
converted_dict = dict(zip(keys, values))
print("\n16. zip() to create dict:", converted_dict)

# End of Demo
print("\n All dictionary methods and operations demonstrated successfully!")
