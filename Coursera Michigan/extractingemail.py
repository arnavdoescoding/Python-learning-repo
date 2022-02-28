from hashlib import new
import re
filename = 'mbox.txt'
fhand = open(filename)
new_file = open('output.txt', 'w')
for line in fhand:
    line = line.rstrip()
    lst = re.findall('.+rom(.+@[\w\.-]+(?:\.[\w]+)+)', line)
    for item in lst:
        string = item[1:] + '\n'
        index = string.find('@')
        slice = string[index + 1:]
        new_file.write(slice)
new_file.close()


        