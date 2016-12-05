import os

files = os.listdir("data/")
output_file = open('output_j.txt', "w")
output_dict = {}

for f in files:
    inp = open("data/{}".format(f), 'r')
    for line in inp.readline():
        for word in line.split():
            if word in output_dict:
                output_dict[word] = 1
            else:
                output_dict[word] += 1

for k,v in output_dict:
    output_file.write("{}, {}\,".format(k, v))