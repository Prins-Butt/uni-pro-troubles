STEPS = 7
total = 0

for i in range(1, STEPS + 1):

    number = int(input("Please enter a whole number: ")) # read a number and convert it to `integer`

    if number % 3 == 0:
        total += number

print("The total for all numbers that are a multiple of 3 is: " + str(total))
