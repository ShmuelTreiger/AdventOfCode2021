import copy
from Input import octopi


class CaveOfOctopi:
    def __init__(self, matrix):
        self.cave = copy.deepcopy(matrix)
        self.neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        self.m = len(self.cave)
        self.n = len(self.cave[0])
        self.flashes = 0

    def flash_octopus(self, i, j):
        for neighbor in self.neighbors:
            a = neighbor[0] + i
            b = neighbor[1] + j
            if 0 <= a < self.m and 0 <= b < self.n:
                self.cave[a][b] += 1
                if self.cave[a][b] == 10:
                    self.flash_octopus(a, b)

    def step(self):
        for i in range(self.m):
            for j in range(self.n):
                self.cave[i][j] += 1
                if self.cave[i][j] == 10:
                    self.flash_octopus(i, j)
        if self.set_flashed_to_0():
            return True

    def set_flashed_to_0(self):
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.cave[i][j] >= 10:
                    self.cave[i][j] = 0
                    self.flashes += 1
                    count += 1
        if count == self.m * self.n:
            return True


if __name__ == "__main__":
    cave = CaveOfOctopi(octopi)
    step = 0
    flag = False
    while not flag or step < 100:
        step += 1
        if cave.step() and not flag:
            flag = True
            print("Simultaneous step:", step)
        if step == 100:
            print("Flashes:", cave.flashes)
