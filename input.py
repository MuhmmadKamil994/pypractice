#  Basic string input
name = input("Enter your name: ")
print("Hello,", name, "!")
print("Type of 'name':", type(name))  # Always str

#  Integer input
age = int(input("Enter your age: "))
print("Your age is:", age)
print("Type of 'age':", type(age))

#  Float input
height = float(input("Enter your height in meters: "))
print("Your height is:", height)
print("Type of 'height':", type(height))

# Boolean input (custom)
# We'll convert user input 'yes/no' to boolean
status_input = input("Are you active? (yes/no): ").strip().lower()
is_active = True if status_input == 'yes' else False
print("Is active:", is_active)
print("Type of 'is_active':", type(is_active))

#  Multiple inputs in one line
numbers = input("Enter multiple numbers separated by space: ").split()
print("Numbers as strings:", numbers)

# Convert to integers
numbers = [int(num) for num in numbers]
print("Numbers as integers:", numbers)

# List of floats input
float_nums = input("Enter floats separated by space: ").split()
float_nums = [float(f) for f in float_nums]
print("List of floats:", float_nums)

#  Tuple input
tuple_input = tuple(input("Enter values for a tuple separated by space: ").split())
print("Tuple:", tuple_input)

#  Set input
set_input = set(input("Enter values for a set separated by space: ").split())
print("Set:", set_input)

#  Dictionary input (key:value pairs)
dict_input = input("Enter key:value pairs separated by comma (e.g. a:1,b:2): ").split(',')
my_dict = {}
for item in dict_input:
    key, value = item.split(':') 
    my_dict[key] = value
print("Dictionary:", my_dict)

# Input with eval() (careful)
# Can evaluate numbers, lists, tuples, dicts
safe_input = input("Enter a Python expression (e.g. [1,2,3] or 10+5): ")
result = eval(safe_input)
print("Evaluated result:", result)
print("Type of result:", type(result))
#correct input checking
y=True
while y==True:
    x=input("Enter a number")
    try:
        x=float(x)
        y=False
    except:
        print("You have entered invalid type")
# End of demo
print("\n All user input examples demonstrated successfully!")
