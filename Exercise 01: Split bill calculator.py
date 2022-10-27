input_bill = float(input("Enter amount of bill: "))
input_people = int(input("Enter number of people: "))
input_tips = int(input("Enter amount of tips (%): "))

count_tips = (input_bill*input_tips/100)/input_people
count_total = (input_bill/2)+count_tips

print(f"Tip amount per person ${count_tips: .2f}")
print(f"Total amount per person ${count_total: .2f}")