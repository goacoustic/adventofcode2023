import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")
file_content = f.read()
input = file_content.split("\n")


print("let's go!")

def calculate_neighbors(row, col):

    nums_found = 0
    visited = set()

    res = 1
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        nr, nc = row + dx, col + dy

        if nr >= 0 and nc >= 0:
            if nr < rows and nc < cols:
                if input[nr][nc].isdigit() and (nr, nc) not in visited:
                    nums_found += 1
                    num, vis = parse_num(nr, nc)
                    res *= num
                    for v in vis:
                        visited.add(v)

    return res if nums_found == 2 else 0

def parse_num(row, col):
    res = int(input[row][col])
    visited = set([(row, col)])

    c = col
    p = 10
    while c > 0 and input[row][c - 1].isdigit():
        c -= 1
        res += int(input[row][c]) * p
        p *= 10
        visited.add((row, c))

    c = col
    while c < cols - 1 and input[row][c + 1].isdigit():
        c += 1
        res *= 10
        res += int(input[row][c])
        visited.add((row, c))

    return (res, visited)

result = 0

rows = len(input)
cols = len(input[0])



for row in range(rows):
    for col in range(cols):
        if input[row][col] == "*":
           result += calculate_neighbors(row, col)


print("result is " + str(result))