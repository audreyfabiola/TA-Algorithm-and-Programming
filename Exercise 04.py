input_lower_bound = eval(input("Enter lower bound: "))


odd_numbers = []
even_numbers = []

while input_lower_bound < 0:
    print(input("Please enter a positive number for lower bound: "))
else: 
    input_upper_bound = eval(input("Enter upper bound: "))
    for i in range(input_lower_bound, input_upper_bound +1):
        if i%2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)

print(f"even numbers = {even_numbers}")
print(f"odd numbers = {odd_numbers}")