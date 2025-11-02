# simple if statement 
x=3
if x>5:
    print("number is greater than five")
else:
    print("number is less than five")

number=6
if number%2:
    print("number is even")
else:
    print("number is odd")

marks=float(input("Enter your marks: "))
if 0<marks>100:
    print("you have entered invalid number please enter betweent(0-100)")
elif 90<=marks<=100:
    print("you got A+ grade")
elif 80<=marks<90:
    print("you got B grade")
elif 70<=marks<80:
    print("you got C grade")
elif 60<=marks<=70:
    print("you got D grade")
else:
 print("you are fail")

salary=45000
experince=4
if experince>3 and salary>=40000:
    print("you are eliglble for job")
else:
    print("you are not eligble")
age=21
country="pakistan"
if age>17 and country=="pakistan":
    print("you are eligble for vote")
else:
    print("you are chil now")
username="kamil"
password="12342" 
if username=="kamil":
    if password=="12342":
        print("access granted")
    else:
        print("invalid password")
else:
    print("Access denied")
name=input("Enter your name: ")
if name:
    print("Hello",name)
else:
    print("you did not enter your name")

income = 60000
credit_score = 720
employment_years = 3
existing_loans = 0

if income >= 50000:
    if credit_score >= 700:
        if employment_years >= 2:
            if existing_loans == 0:
                print("Loan Approved: Excellent Standing ")
            elif existing_loans <= 2:
                print("Loan Approved with Caution ")
            else:
                print("Loan Denied: Too many existing loans ")
        else:
            print("Loan Denied: Not enough job stability ")
    else:
        print("Loan Denied: Credit score too low ")
else:
    if income >= 30000:
        print("Loan Pending Review 🔍")
    else:
        print("Loan Denied: Insufficient income ")
