from Input import coordinates, folds


class Paper:
    def __init__(self, initial_height, initial_length, input_coordinates):
        self.height = initial_height
        self.length = initial_length

        self.grid = []
        for _ in range(self.height):
            dots = [False] * self.length
            self.grid.append(dots)

        for coordinate in input_coordinates:
            x = coordinate[0]
            y = coordinate[1]
            self.grid[y][x] = True

    def fold_vertically(self, axis):
        for y in range(self.height):
            for x in range(axis):
                self.grid[y][x] = self.grid[y][x] or self.grid[y][self.length - (x + 1)]

        self.length = axis

    def fold_horizontally(self, axis):
        for y in range(axis):
            for x in range(self.length):
                self.grid[y][x] = self.grid[y][x] or self.grid[self.height - (y + 1)][x]

        self.height = axis


if __name__ == "__main__":
    initial_length = 1311
    initial_height = 895
    manual = Paper(initial_height=initial_height, initial_length=initial_length, input_coordinates=coordinates)

    first_pass = True
    for fold in folds:
        if fold[0] == "x":
            manual.fold_vertically(fold[1])
        else:
            manual.fold_horizontally(fold[1])
        if first_pass:
            first_pass = False
            count = 0
            for j in range(manual.height):
                for i in range(manual.length):
                    count += manual.grid[j][i]
            print(count)

    for row in manual.grid[: manual.height + 1]:
        line = []
        for bit in row[: manual.length + 1]:
            if bit:
                line.append(111)
            else:
                line.append(" ")
        print(line)
