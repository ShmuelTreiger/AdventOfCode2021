from Input import fish

fish_count = [0] * 9

for f in fish:
    fish_count[f] += 1

for day in range(80):
    x = fish_count.pop(0)
    fish_count.append(x)
    fish_count[6] += x

print(sum(fish_count))

for day in range(256 - 80):
    x = fish_count.pop(0)
    fish_count.append(x)
    fish_count[6] += x

print(sum(fish_count))
