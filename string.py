str1="hello world!"
str2='The Islamia University of Bhawalpur'
str3='''this is multi 
line string.
'''

print(str1)
print(str2[0:])
print(str3)
print(str1.lower())
print(str1.upper())
print(str1.swapcase())
print(str1.title())
print(str1.capitalize())
print("hello".isalpha())
print("HELLO".isupper())
print("32342".isnumeric())
print("hello123".isalnum())
print(str1.strip())
print(str2.find("of"))
print(str1.replace("hello","HI"))
print(str1.split(" "))
print(str1.center(30,"-"))
name="Malik Kamil"
age=21
print(f"my name is {name}, and i am {age} year old")
print("my name is {}, and i am {} year old".format(name,age))
print("my name is %s, and i am %d year old" %(name,age))
trans=str1.maketrans({'H':'K','W':'L'})
print(str1.translate(trans))
def demo_func():
    """This is a docstring (documentation string)."""
    pass

print("\n--- Docstring ---")
print(demo_func.__doc__)