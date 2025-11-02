a=6
b=5
print("---Arithmatic operators---")
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print("---comparison Operators---")
print(a>b)
print(a<b)
print(a!=b)
print(a==b)
print(a<=b)
print(a>=b)
print("---assignment Operators")
a+=4
print(a)
a*=4
print(a)
a/=4
print(a)
a%=4
print(a)
a**=2
print(a)
print("---logical Operators---")
x=4
print(x>5 and x<3)
print(x>5 or x<6)
print( not (x<5))
print("---Bitwise Operators---")
c=5
d=2
print(c&d)
print(c|d)
print(c^d)
print(~d)
print(c<<3)
print(c>>3)
x=["kamil",21]
y=["kamil",21]
z=x
print(x is z)
print(x is y)
print(x==y)
print(x is not y)
print(id(x))
print(id(y))
print(id(z))
# Precedence order (highest to lowest):
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary +, - , ~
# 4. Multiplication *, Division /, Floor Division //, Modulus %
# 5. Addition +, Subtraction -
# 6. Bitwise shifts << >>
# 7. Bitwise AND &
# 8. Bitwise XOR ^
# 9. Bitwise OR |
# 10. Comparisons (>, <, >=, <=, ==, !=)
# 11. Logical NOT
# 12. Logical AND
# 13. Logical OR
# 14. Assignment (=, +=, -=, etc.)
# 15. Identity & Membership operators