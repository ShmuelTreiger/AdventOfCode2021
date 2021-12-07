from Input import lines

grid = []
size = 1000
for i in range(size):
    grid.append([0] * size)


for pair in lines:
    pair = sorted(pair)  # sorts by x
    x1, y1 = pair[0]
    x2, y2 = pair[1]

    if x1 == x2:
        ys = sorted([y1, y2])
        for num in range(ys[0], ys[1] + 1):
            grid[num][x1] += 1
    if y1 == y2:
        for num in range(x1, x2 + 1):
            grid[y1][num] += 1

count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] >= 2:
            count += 1
print(count)

for pair in lines:
    pair = sorted(pair)  # sorts by x
    x1, y1 = pair[0]
    x2, y2 = pair[1]
    if (x1 - x2) == (y1 - y2):
        while x1 <= x2:
            grid[y1][x1] += 1
            x1 += 1
            y1 += 1

    if (x1 - x2) == (y2 - y1):
        while x1 <= x2:
            grid[y1][x1] += 1
            x1 += 1
            y1 -= 1

count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] >= 2:
            count += 1
print(count)
