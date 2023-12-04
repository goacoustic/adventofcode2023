import os

f = open(os.path.join(os.path.dirname(__file__), "input2.txt"), "r")
file_content = f.read()
input = file_content.split("\n")


print("let's go!")

result = 0

total_n = len(input)
scratchcard_amount = [1] * total_n

for i, line in enumerate(input):

    split = line.split(":")[1].split(" | ")

    wining = set([int(n) for n in split[0].split(" ") if n])
    we_have = [int(n) for n in split[1].split(" ") if n]

    matching_nums = [n for n in we_have if n in wining]


    for di in range(1, len(matching_nums) + 1):
        if i + di == total_n:
            break

        scratchcard_amount[i + di] += scratchcard_amount[i]



result = sum(scratchcard_amount)
print("result is " + str(result))