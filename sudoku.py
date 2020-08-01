sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
new =[]
new.append("-----------")
for j in sudoku:
    j.insert(3, '|')
    j.insert(7, '|')

    for i in sudoku:




        new.append(i)

        if i ==sudoku[2]:
            new.append("-----------")

        elif i==sudoku[5]:
            new.append("-----------")
        elif i==sudoku[8]:
            new.append("-----------")

for i in new:print(*i)

