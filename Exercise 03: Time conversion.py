input_seconds = int(input("Enter the number of seconds: "))

hours = input_seconds//3600
minutes = (input_seconds//60) %60
seconds = input_seconds%60

print(f"Result: {hours}:{minutes}:{seconds}") 