import os
import sys

files = os.listdir("data/")
output_file = open('output_j.txt', "w")
output_dict = {}

for f in files:
    inp = open("data/{}".format(f), 'r')
    # print("File = {}".format(inp))
    for line in inp.readlines():
        for word in line.split():
            if word not in output_dict:
                output_dict[word] = 1
            else:
                output_dict[word] += 1

for key in output_dict:
    output_file.write("{}, {}\n".format(key, output_dict[key]))
