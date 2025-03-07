def find_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

numbers = [1,2,3,4,5,6,7,8,9]
average = find_average(numbers)
print(f"The average of the numbers is: {average}")

print("Round of the average to 2 decimal places: ", round(average, 2))
