input_number = int(input("Enter a number: "))

if input_number==2 or input_number==3 or input_number==7 or input_number==11:
    print("The number " + str(input_number) + " is a prime number")
elif input_number%2 or input_number%3 or input_number%7 or input_number%11 == 0:
    print("The number " + str(input_number) + " is not a prime number")
else:
    print("The number " + str(input_number) + " is a prime number")