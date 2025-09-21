
# Exercise 5: Accept a list of 5 float numbers as an input from the user

numbers = []

for i in range(5):
    num = float(input(f"enter numbers {i+1} : "))
    numbers.append(num)
print(numbers)