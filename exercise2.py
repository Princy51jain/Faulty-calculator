# FAULTY  CALCULATOR -------------------->>>>>>>>
# 45*3=555, 56+9=77, 56/6=4

import sys


def calc(num1, num2, oper):
    if num1 == 45 and num2 == 3 and oper == '*':
        print(555)
    elif num1 == 56 and num2 == 9 and oper == '+':
        print(77)
    elif num1 == 56 and num2 == 6 and oper == '/':
        print(4)

    elif oper == '+':
        print(num1 + num2)
    elif oper == '-':
        print(num1 - num2)
    elif oper == '*':
        print(num1 * num2)
    elif oper == '/':
        print(num1 / num2)
    elif oper == '%':
        print(num1 % num2)

    else:
        print("Please check your input again!!")


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
oper = input("Enter the operator: ")
calc(num1, num2, oper)

inp = input("Do you want to continue ?(y/n): ")

if inp == 'y':
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    oper = input("Enter the operator: ")
    calc(num1, num2, oper)
elif inp == 'n':
    sys.exit()
else:
    print("Invalid input!!")
