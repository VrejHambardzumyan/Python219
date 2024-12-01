def sumOfElemets(numbers, excludeNegative = False):
    if excludeNegative:
        numbers = [nums for nums in numbers if nums >= 0]
    return sum(numbers)

userInput = input("Enter space-separated numbers: ")
numbers = list(map(int,userInput.split()))

excludeNegativeInput = input("Exclude negative numbers? (yes/no): ").strip().lower()
excludeNegative = excludeNegativeInput == "yes"

result = sumOfElemets(numbers, excludeNegative)
print(f"The sum of elements is {result}")