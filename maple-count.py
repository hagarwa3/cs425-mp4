import os

files = os.listdir("data/")
output_file = open('output_m.txt', "w")


for f in files:
    inp = open("data/{}".format(f), 'r')
    for line in inp.readline():
        for word in line.split():
            output_file.write("({}, 1)\n".format(word))
