# Get the input values from the 'adventofcode.txt' textfile and return lines as array
def get_input():
    with open('adventofcode.txt') as textfile:
        return textfile.readlines()

input_values = get_input()
last_value = 999999
number_of_increases = 0

for i in range(1, len(input_values) - 1):
    value = int(input_values[i - 1]) + int(input_values[i]) + int(input_values[i + 1])

    if value > last_value:
        number_of_increases += 1

    last_value = int(value)

# Print the result
print(number_of_increases)
