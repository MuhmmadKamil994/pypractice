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
