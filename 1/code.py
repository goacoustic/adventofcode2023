import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")
input = f.read()

result = 0

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

print("let's go!")

def match(w: str, i: int, shouldMathchForward):

    for num_i in range(len(nums)):
        number = nums[num_i]
        number_len = len(number)

        if shouldMathchForward:
            if i >= number_len:
                #print("matching forward {} with {}".format(number, w[i-number_len:i]))
                if w[i-number_len:i] == number:
                    return num_i + 1

        else:
            if i + number_len < len(w):
                #print("matching backward {} with {}".format(number, w[i+1:i+number_len+1]))
                if w[i+1:i+number_len+1] == number:
                    return num_i + 1

    if w[i].isdigit():
        return int(w[i])

    return 0

for w in input.split("\n"):

    line_res = 0
    for i in range(len(w)):
        res = match(w, i, True)
        if res:
            line_res = res * 10
            break

    for i in range(len(w) - 1, -1, -1):
        res = match(w, i, False)
        if res:
            #print("mathced right - {}".format(res))
            line_res += res
            break

    print("{} => {}".format(w, line_res))
    result += line_res

print("result is " + str(result))