d1 = {}
d2 = {}
d3 = {}
index = 1
a = 1
name = ''
quiz = ''

answers = {"A" : "0", "B": "1", "C": "2", "D": "3"}

with open("textfile.txt") as f:
    name = f.readline()
    quiz = f.readline()

    for line in f:
        if a < 5:
            (key, val) = str(index), line.split()[0]
            d1[(key)] = answers[val]
            a += 1
            index += 1
        elif a == 5:
            index = 1
            (key, val) = str(index), line.split()[0]
            d2[(key)] = answers[val]
            a += 1
            index += 1
        elif a > 5 and a <= 8:
            (key, val) = str(index), line.split()[0]
            d2[(key)] = answers[val]
            a += 1
            index += 1
        elif a == 9:
            index = 1
            (key, val) = str(index), line.split()[0]
            d3[(key)] = answers[val]
            a += 1
            index += 1
        elif a > 9 and a < 13:
            (key, val) = str(index), line.split()[0]
            d3[(key)] = answers[val]
            a += 1
            index += 1

         
print(d1)
print(d2)
print(d3)
print(name)
print(quiz)

exec(open('grader.py').read())

