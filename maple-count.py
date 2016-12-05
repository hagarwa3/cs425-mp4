import os

files = os.listdir("data/")
output_file = open('output_m.txt', "w")
count = 0

for f in files:
    inp = open("data/{}".format(f), 'r')
    print("File = {}".format(inp))
    for line in inp.readlines():
        for word in line.split():
            count += 1
            output_file.write("({}, {})\n".format(word, 1))

output_file.close()
print("Number of outputs = {}".format(count))