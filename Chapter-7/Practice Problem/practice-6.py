num = int(input("Enter a number to check the factorial of that number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is", factorial)