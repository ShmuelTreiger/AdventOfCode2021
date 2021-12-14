# Actual solution
from collections import Counter, defaultdict
from Input import initial_string, rules

char_counter = Counter(initial_string)

key_counter = defaultdict(lambda: 0)

keys = rules.keys()
for i in range(len(initial_string)):
    key = initial_string[i : i + 2]
    if key in keys:
        key_counter[key] += 1

replacement_strings = {}
for key in rules:
    char = rules[key]
    replacement_strings[key] = (key[0] + char, char + key[1])

for step in range(40):
    new_key_counter = defaultdict(lambda: 0)
    for key in key_counter:
        char = rules[key]
        count = key_counter[key]
        char_counter[char] += count

        for string in replacement_strings[key]:
            if string in keys:
                new_key_counter[string] += count

    key_counter = new_key_counter

    if step == 9 or step == 39:
        print(max(char_counter.values()) - min(char_counter.values()))
