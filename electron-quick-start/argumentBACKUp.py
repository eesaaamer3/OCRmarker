
d = {}
a = 0
index = 0
name = ''
quiz = ''

with open("textfile.txt") as f:
    name = f.readline()
    quiz = f.readline()

    for line in f:
        a += 1
        if (a > 2):
            index += 1
            (key, val) = index, line.split()
            d[(key)] = val


print(d)
print(name)
print(quiz)

