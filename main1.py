print("Average Finder")
count = int(input("Enter the number of numbers you want to find the average of: "))
numbers = []

for i in range (count):
    num = int(input(f"Enter the {i+1}th number: "))
    numbers.append(num)

sum_of_numbers = 0
for n in numbers:
    sum_of_numbers = sum_of_numbers+n
average= sum_of_numbers/count
print(f"The average of your numbers is {average}!")

#average = (num1+num2+num3)/3
#print(f"The average of {num1}, {num2}, and {num3} is {average}")