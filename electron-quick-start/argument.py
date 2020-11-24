d1 = {}
d2 = {}
d3 = {}
index = 1
a = 1
name = ''
quiz = ''

# Assigns student answers on a bubble sheet test a numerical value 
answers = {"A" : "0", "B": "1", "C": "2", "D": "3"}

with open("textfile.txt") as f:
    # Reads the first two lines of the textfile, which should be the name of the student and the quiz title
    name = f.readline()
    quiz = f.readline()

    # From this point on, the script will read from the third line of the test file    
    # The following code splits the data into three seperate dictionaries to allow for simplicity and organization
    # it also matches up with the way the grading algorithm is executed in "grader.py"
    for line in f:
        if a < 5:
            # Takes each answer from the answer key text file and assigns it a numerical value
            # It appends the result into the first dictionary
            (key, val) = str(index), line.split()[0]
            d1[(key)] = answers[val]
            a += 1
            index += 1
        elif a == 5:
            # Takes each answer from the answer key text file and assigns it a numerical value
            # It appends the result into the second dictionary
            index = 1
            (key, val) = str(index), line.split()[0]
            d2[(key)] = answers[val]
            a += 1
            index += 1
        elif a > 5 and a <= 8:
            # Takes each answer from the answer key text file and assigns it a numerical value
            # It appends the result into the second dictionary
            (key, val) = str(index), line.split()[0]
            d2[(key)] = answers[val]
            a += 1
            index += 1
        elif a == 9:
            # Takes each answer from the answer key text file  and assigns it a numerical value
            # It appends the result into the third dictionary
            index = 1
            (key, val) = str(index), line.split()[0]
            d3[(key)] = answers[val]
            a += 1
            index += 1
        elif a > 9 and a < 13:
            # Takes each answer from the answer key text file and assigns it a numerical value
            # It appends the result into the third dictionary
            (key, val) = str(index), line.split()[0]
            d3[(key)] = answers[val]
            a += 1
            index += 1

         
#print(d1)
#print(d2)
#print(d3)
#print(name)
#print(quiz)

# Executes the grader.py python file, which contains the main algorithm 
exec(open('grader.py').read())

