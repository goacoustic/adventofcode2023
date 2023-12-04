import os

f = open(os.path.join(os.path.dirname(__file__), "input2.txt"), "r")
file_content = f.read()
input = file_content.split("\n")


print("let's go!")

result = 0

for line in input:

    split = line.split(":")[1].split(" | ")

    print(split[1].split(" "))

    wining = set([int(n) for n in split[0].split(" ") if n])
    we_have = [int(n) for n in split[1].split(" ") if n]

    num = [n for n in we_have if n in wining]

    if num:
        result += 2 ** (len(num) - 1)



print("result is " + str(result))