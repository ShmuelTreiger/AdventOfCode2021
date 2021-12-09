from Input import signal_patterns

count = 0
unique_line_count = {2, 3, 4, 7}
for signal_pattern in signal_patterns:
    output_values = signal_pattern[1]
    for value in output_values:
        if len(value) in unique_line_count:
            count += 1

print(count)

total = 0
for signal_pattern in signal_patterns:
    value_map = {}
    signals = sorted([tuple(sorted(pattern)) for pattern in signal_pattern[0]], key=len)
    seven = set(signals[1])
    eight = set(signals[9])
    value_map[signals[0]] = 1  # len 2
    value_map[signals[1]] = 7  # len 3
    value_map[signals[2]] = 4  # len 4
    value_map[signals[9]] = 8  # len 7

    if seven.issubset(signals[3]):  # 7 is a subset of 3, but not of 2 or 5
        three = set(signals[3])
        three_index = 3
        value_map[signals[3]] = 3
    elif seven.issubset(signals[4]):  # 7 is a subset of 3, but not of 2 or 5
        three = set(signals[4])
        three_index = 4
        value_map[signals[4]] = 3
    elif seven.issubset(signals[5]):  # 7 is a subset of 3, but not of 2 or 5
        three = set(signals[5])
        three_index = 5
        value_map[signals[5]] = 3

    if not seven.issubset(signals[6]):  # 7 is a subset of 9 and 0, but not of 6
        value_map[signals[6]] = 6
        if three.issubset(signals[7]):  # 3 is a subset of 9, but not 0
            nine = set(signals[7])
            value_map[signals[7]] = 9
            value_map[signals[8]] = 0
        else:
            nine = set(signals[8])
            value_map[signals[7]] = 0
            value_map[signals[8]] = 9
    elif not seven.issubset(signals[7]):  # 7 is a subset of 9 and 0, but not of 6
        value_map[signals[7]] = 6
        if three.issubset(signals[6]):  # 3 is a subset of 9, but not 0
            nine = set(signals[6])
            value_map[signals[6]] = 9
            value_map[signals[8]] = 0
        else:
            nine = set(signals[8])
            value_map[signals[6]] = 0
            value_map[signals[8]] = 9
    elif not seven.issubset(signals[8]):  # 7 is a subset of 9 and 0, but not of 6
        value_map[signals[8]] = 6
        if three.issubset(signals[6]):  # 3 is a subset of 9, but not 0
            nine = set(signals[6])
            value_map[signals[6]] = 9
            value_map[signals[7]] = 0
        else:
            nine = set(signals[7])
            value_map[signals[6]] = 0
            value_map[signals[7]] = 9

    difference = (eight - nine).pop()
    if difference in signals[3]:  # difference between 9 and 8 in and 2, but not 3 or 5
        value_map[signals[3]] = 2
        if three_index == 4:
            value_map[signals[5]] = 5
        else:
            value_map[signals[4]] = 5
    elif difference in signals[4]:  # difference between 9 and 8 in and 2, but not 3 or 5
        value_map[signals[4]] = 2
        if three_index == 5:
            value_map[signals[3]] = 5
        else:
            value_map[signals[5]] = 5
    elif difference in signals[5]:  # difference between 9 and 8 in and 2, but not 3 or 5
        value_map[signals[5]] = 2
        if three_index == 3:
            value_map[signals[4]] = 5
        else:
            value_map[signals[3]] = 5

    output_values = signal_pattern[1]
    total += 1000 * value_map[tuple(sorted(output_values[0]))]
    total += 100 * value_map[tuple(sorted(output_values[1]))]
    total += 10 * value_map[tuple(sorted(output_values[2]))]
    total += 1 * value_map[tuple(sorted(output_values[3]))]

print(total)
