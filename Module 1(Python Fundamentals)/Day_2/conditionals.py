# Basic if
age = 20

if age >= 18:
    print("Adult")

# if else
marks = 45

if marks >= 50:
    print("Pass")
else:
    print("Fail")

# if elif else
score = 87

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs Improvement")

# Nested if
age = 25
salary = 60000

if age >= 18:
    if salary > 50000:
        print("Eligible")