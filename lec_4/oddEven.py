numbers = list(map(int,input("Enter the numbers: ").split()))

evenNums = [num for num in numbers if num % 2 == 0]
oddNums = [num for num in numbers if num % 2 != 0]

print (f"Even nubers: {evenNums}")
print (f"Odd numbers: {oddNums}")