'''
create a calculator program using functions, loops, if and else. Basically everything u have learnt so far. 
Push ur answer to a repo and WA or Discord the link to ko Alvin.
DUE DATE: 22/10/2022 11.59 PM
'''

def calculate(x,y,operator):
    if operator == "+":
        print(x+y)
    elif operator == "-":
        print(x-y)
    elif operator == "/":
        print(x/y)
    elif operator == "%":
        print(x%y)
    elif operator == "*":
        print(x*y)
    elif operator == "**":
        print(x**y)
    else:
        print("Please enter an appropriate equation.")

calculate_again = "Yes"
while calculate_again == "Yes":
    x = eval(input(print("Enter the first number: ")))
    y = eval(input(print("Enter the second number: ")))
    print("Operator Choices: +, -, /, *, **, %")
    operator = input(print("Enter an operator: "))
    calculate(x,y,operator)

    calculate_again = input(print("Do you want to calculate again? Yes/No: "))

else:
    print("Thank you for using the calculator, bye!")


    

