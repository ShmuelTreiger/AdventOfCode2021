with open("Input.txt", "r") as file:
    lines = file.readlines()

    matches = {"(": ")", "[": "]", "{": "}", "<": ">"}
    corrupted_character_values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    completion_string_values = {")": 1, "]": 2, "}": 3, ">": 4}
    openers = matches.keys()
    total = 0
    completion_string_scores = []
    for line in lines:
        line = line.strip()
        stack = []
        for char in line:
            if char in openers:
                stack.append(char)
            else:
                last = stack.pop(-1)
                if char != matches[last]:
                    total += corrupted_character_values[char]
                    stack = []
                    break
        completion_string_points = 0
        while stack:
            completion_string_points *= 5
            last = stack.pop(-1)
            complement = matches[last]
            completion_string_points += completion_string_values[complement]
        if completion_string_points:
            completion_string_scores.append(completion_string_points)

    print(total)
    print(sorted(completion_string_scores)[len(completion_string_scores) // 2])
