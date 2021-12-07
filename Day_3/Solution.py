import numpy
from Input import lines_of_binary

solution = [0] * len(lines_of_binary[0])
for y in lines_of_binary:
    solution = numpy.add(solution, y)

solution *= 2

gamma_rate = ["0b"]
epsilon_rate = ["0b"]
line_count = len(lines_of_binary)
for num in solution:
    if num > line_count:
        gamma_rate.append("1")
        epsilon_rate.append("0")
    else:
        gamma_rate.append("0")
        epsilon_rate.append("1")

gamma_rate = "".join(gamma_rate)
epsilon_rate = "".join(epsilon_rate)
gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
print("Gamma Rate", gamma_rate)
print("Epsilon Rate", epsilon_rate)
print("Solution", gamma_rate * epsilon_rate)


sorted_lines = sorted(lines_of_binary)
index = 0
while len(sorted_lines) > 1:
    beginning = 0
    end = len(sorted_lines) - 1
    middle = int(end / 2)
    if (beginning - end) % 2 == 1:  # even number of rows remaining
        middle_plus_one = middle + 1
        if (
            sorted_lines[middle_plus_one][index] > sorted_lines[middle][index]
        ):  # first is 0, second is 1
            sorted_lines = sorted_lines[middle_plus_one:]
            index += 1
            continue
    if sorted_lines[middle][index] == 0:  # should really do binary search
        while sorted_lines[-1][index] == 1:
            sorted_lines.pop(-1)
    else:
        while sorted_lines[0][index] == 0:
            sorted_lines.pop(0)
    index += 1

oxygenator_rating = int("0b" + "".join(str(digit) for digit in sorted_lines[0]), 2)

sorted_lines = sorted(
    lines_of_binary
)  # if used binary search, wouldn't have to sort again
index = 0
while len(sorted_lines) > 1:
    beginning = 0
    end = len(sorted_lines) - 1
    middle = int(end / 2)
    if (beginning - end) % 2 == 1:  # even number of rows remaining
        middle_plus_one = middle + 1
        if (
            sorted_lines[middle_plus_one][index] > sorted_lines[middle][index]
        ):  # first is 0, second is 1
            sorted_lines = sorted_lines[:middle_plus_one]
            index += 1
            continue
    if sorted_lines[middle][index] == 0:
        while sorted_lines[0][index] == 0:
            sorted_lines.pop(0)
    else:
        while sorted_lines[-1][index] == 1:
            sorted_lines.pop(-1)
    index += 1

c02_scrubber_rating = int("0b" + "".join(str(digit) for digit in sorted_lines[0]), 2)


print("Oxygenator Rating", oxygenator_rating)
print("C02 Scrubber Rating", c02_scrubber_rating)
print("Solution", oxygenator_rating * c02_scrubber_rating)
