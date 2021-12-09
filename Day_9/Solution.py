import itertools
import math

from Input import cave_floor
from collections import deque
import heapq

risk_level = 0
m = len(cave_floor)
n = len(cave_floor[0])
for i in range(m):
    for j in range(n):
        flag = True
        neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for neighbor in neighbors:
            if 0 <= neighbor[0] < m and 0 <= neighbor[1] < n:
                if cave_floor[neighbor[0]][neighbor[1]] <= cave_floor[i][j]:
                    flag = False
                    break
        if flag:
            risk_level += 1 + cave_floor[i][j]

print(risk_level)

heap = [0, 0, 0]
for i in range(m):
    for j in range(n):
        stack = deque()
        stack.append([i, j])
        basin_size = 0
        while stack:
            x, y = stack.popleft()
            if cave_floor[x][y] != 9:
                cave_floor[x][y] = 9
                basin_size += 1
                neighbors = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
                for neighbor in neighbors:
                    if 0 <= neighbor[0] < m and 0 <= neighbor[1] < n:
                        stack.append(neighbor)

        heapq.heappush(heap, basin_size)
        heapq.heappop(heap)

print(math.prod(heap))
