print("Enter 3 numbers separated by commas")
numbers = input("Enter the numbers: ")
num1, num2, num3 = numbers.split(",")
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3
print("The largest number is:", largest)
print("The smallest number is:", smallest)
