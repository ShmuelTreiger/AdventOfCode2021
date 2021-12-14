# Brute force with minor optimization; can do 21 steps
from collections import Counter
from Input import initial_string, rules


class Node:
    def __init__(self, char):
        self.char = char
        self.next = None

    def __str__(self):
        x = [self.char]
        runner = self
        while runner.next:
            runner = runner.next
            x.append(runner.char)
        return "".join(x)


counter = Counter(initial_string)

head = Node(initial_string[0])
runner = head
for i in range(1, len(initial_string)):
    char = initial_string[i]
    new_node = Node(char)
    runner.next = new_node
    runner = runner.next


keys = rules.keys()
for _ in range(10):
    last_node = head
    while last_node.next:
        next_node = last_node.next

        if not last_node.char and not next_node.char:
            last_node.next = next_node.next
            continue

        key = last_node.char + next_node.char
        if key in keys:
            new_char = rules[key]
            new_node = Node(new_char)
            counter[new_char] += 1
            last_node.next = new_node
            new_node.next = next_node
        else:
            next_key = next_node.char + next_node.next.char
            if next_key not in keys:
                next_node.char = None

        last_node = next_node

print(max(counter.values()) - min(counter.values()))
