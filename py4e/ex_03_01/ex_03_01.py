"""
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

workHours = int(input())
rate =  int(input())

if workHours > 40:
    pay = (int(workHours) - 40) * int(rate)
    overTimePay = 
    print(pay)
else:
    pay = int(workHours) * int(rate)
    print(pay)



