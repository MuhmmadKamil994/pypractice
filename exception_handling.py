number=int(input("Enter a nubmer : "))
try:
    result=10/number
    print(f"The division of number is {result}")
except ZeroDivisionError:
    print("The number cann't divided by zero")
except ValueError as e:
    print("The number is invalid")

file=open('test.py',"r")
content=file.read()
try:
    print("file is opened")
except FileNotFoundError:
    print("file not opened")
else:
    print("file is readed successfuly")
finally:
    if 'file' in locals():
     file.close
     print("file operation is complete")
class InvalidAgeError(Exception):
   def __init__(self, age, message="Age must be between 18 and 100"):
      self.age = age
      self.message = message
      super().__init__(self.message)

def set_age(age):
   if age < 18 or age > 100:
      raise InvalidAgeError(age)
   print(f"Age is set to {age}")

try:
   set_age(19)
except InvalidAgeError as e:
   print(f"Invalid age: {e.age}. {e.message}")