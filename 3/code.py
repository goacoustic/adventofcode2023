import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")
file_content = f.read()
input = file_content.split("\n")


print("let's go!")

def is_neighbor_symbol(row, col):

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        nr, nc = row + dx, col + dy

        if nr >= 0 and nc >= 0:
            if nr < rows and nc < cols:
                if not input[nr][nc].isdigit() and input[nr][nc] != ".":
                    return True

    return False

result = 0

rows = len(input)
cols = len(input[0])

cur_num = 0
has_parts = False

for row in range(rows):
    for col in range(cols):
        if input[row][col].isdigit():
            cur_num *= 10
            cur_num += int(input[row][col])
            if not has_parts:
                has_parts = is_neighbor_symbol(row, col)

        if cur_num and (not input[row][col].isdigit() or col == cols - 1):
            if has_parts:
                has_parts = False
                result += cur_num

            cur_num = 0



print("result is " + str(result))