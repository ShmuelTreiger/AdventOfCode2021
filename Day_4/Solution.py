from Input import drawn_numbers, boards

flag = False
for number in drawn_numbers:
    for i in reversed(range(len(boards))):
        board = boards[i]
        result = board.check_value(number)
        if result >= 0:
            if not flag:
                flag = True
                print(result * number)

            if len(boards) == 1:
                print(result * number)
                exit()
            boards.pop(i)
