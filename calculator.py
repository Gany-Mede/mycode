#!/usr/bin/env python3
print("You will be asked for two numbers and an operator to calculate the end result: \n")
result = 0
first = 0
second = 0
operator = ""

def add(a,b):
    global result
    result = a + b

def subtract(a, b):
    global result
    result = a -b

def multiply(a,b):
    global result
    result = a * b

def divide(a,b):
    global result
    result = a / b

def prompt():
    global first
    global operator
    global second
    try: 
        first= float(input("Enter First number: "))
        operator =  input("Enter operator: +, -, /, *: ")
        second = float(input("Enter Second number:  "))
    except:
        print("Looks like you typed a wrong value for one of the numers, try again from the beginning!\n")
        prompt()
    if operator == "+":
        add(first, second)
    elif operator == '-':
        subtract(first, second)
    elif operator == '*':
        multiply(first, second)
    elif operator == '/':
        divide(first, second)
    else:
        print("You entered wrong operator, try again\n")
        prompt()

prompt()


print(f"The result is {result}")





