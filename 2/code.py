import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")
input = f.read()


print("let's go!")

def parse_subset(subset: str):

    cubes = subset.split(",")
    res = [0, 0, 0] #rgb

    colors = ["red", "green", "blue"]

    for cube in cubes:
        for i in range(len(colors)):
            color = colors[i]
            if cube.endswith(color):
                res[i] = int(cube.replace(color, ""))

    return res

result = 0
for w in input.split("\n"):

    col = w.split(":")
    game_id = int(col[0].replace("Game ", ""))

    subsets = col[1].split(";")

    min_colors = [0, 0, 0]
    for subset in subsets:
        colors = parse_subset(subset)
        for i in range(len(colors)):
            min_colors[i] = max(min_colors[i], colors[i])
    else:
        #print(f"{game_id} is valid")
        result += min_colors[0] * min_colors[1] * min_colors[2]
    


print("result is " + str(result))