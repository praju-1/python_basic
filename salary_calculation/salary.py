"importing another file"
from emp import *

"Taking input from user"
basic = float(input("Enter you basic salary : "))

"This will calculate your gross salary"
Gross = basic + ta(basic) + hra(basic)

"This will calculate your net salary"
Net_salary = Gross - pf(basic) - itax(Gross)

"This will calculate your bonus"
bonus = basic * 3

print("\nYour Gross salary is : ", Gross)
print("\nYour Net salary is : ", Net_salary)
print("\nYour bonus is : ", bonus)


#If you want to check each detail value of section
print("\nThe amount deducted for your pf is : ", pf(basic))
print("\nThe tax deducted from you salary is : ", itax(Gross))
print("\nThe travelling allowance you get is : ", ta(basic))
print("\nThe House rent allowance is : ", hra(basic))