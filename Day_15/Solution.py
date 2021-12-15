from collections import defaultdict

from Input import risk_level


def multiply_board(board, factor):
    new_board = []
    for _ in range(factor):
        new_row = [[]] * factor
        new_board.append(new_row)

    current_coordinates = {(0, 0)}
    while current_coordinates:
        for coordinate in current_coordinates:
            i, j = coordinate
            new_board[i][j] = board

        board = increment_board(board)
        current_coordinates = increment_coordinates(current_coordinates, factor)

    return combine_board(new_board)


def combine_board(multi_dimensional_board):
    combined_board = []
    for i in range(len(multi_dimensional_board)):
        row_of_boards = multi_dimensional_board[i]
        left_most_board_in_row_of_boards = row_of_boards[0]
        for j in range(1, len(row_of_boards)):
            individual_board = row_of_boards[j]
            for individual_row in range(len(individual_board)):
                left_most_board_in_row_of_boards[individual_row] += individual_board[individual_row]
        combined_board += left_most_board_in_row_of_boards
    return combined_board


def increment_coordinates(coordinates, maximum):
    new_coordinates = set()
    for coordinate in coordinates:
        first_new_coordinate = tuple(map(sum, zip(coordinate, (1, 0))))
        second_new_coordinate = tuple(map(sum, zip(coordinate, (0, 1))))

        if first_new_coordinate[0] < maximum:
            new_coordinates.add(first_new_coordinate)
        if second_new_coordinate[1] < maximum:
            new_coordinates.add(second_new_coordinate)

    return new_coordinates


def increment_board(board):
    new_board = []
    for row in board:
        new_row = []
        for col in row:
            new_val = col + 1
            if new_val == 10:
                new_val = 1
            new_row.append(new_val)
        new_board.append(new_row)
    return new_board


original_m = len(risk_level)
original_n = len(risk_level[0])
final_m = original_m * 5
final_n = original_n * 5

board = multiply_board(risk_level, 5)

visiting = defaultdict(list)
visiting[0].append((0, 0))
visited = {(0, 0)}

neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
found = False
while visiting.keys():
    lowest = min(visiting.keys())
    visit_coords = visiting[lowest].pop(-1)
    if not visiting[lowest]:
        visiting.pop(lowest)

    i = visit_coords[0]
    j = visit_coords[1]
    for neighbor in neighbors:
        a = i + neighbor[0]
        b = j + neighbor[1]
        if 0 <= a < final_m and 0 <= b < final_n and (a, b) not in visited:
            value = board[a][b]
            total = lowest + value

            if a == original_m - 1 and b == original_n - 1:
                print("Original end:", total)
                if found:
                    exit()
                else:
                    found = True

            if a == final_m - 1 and b == final_n - 1:
                print("Final end:", total)
                if found:
                    exit()
                else:
                    found = True

            visiting[total].append((a, b))
            visited.add((a, b))
