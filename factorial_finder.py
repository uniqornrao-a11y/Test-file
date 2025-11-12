num_for_factorial=int(input("Enter the number that you want to find the factorial of: "))

product = 1
for i in range(1, num_for_factorial+1):
    product = product * i

print(f"Factorial = {product}")