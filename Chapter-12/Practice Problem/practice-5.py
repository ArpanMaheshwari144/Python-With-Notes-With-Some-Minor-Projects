num = int(input("Enter a number you want to print the table: "))

# list comprehension
table = [num*i for i in range(1, 11)]
print(table)
with open('text/Tables.txt', 'a') as f:
    f.write(str(table))
    f.write('\n')
