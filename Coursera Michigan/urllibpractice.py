import urllib.request , urllib.parse , urllib.error

link = 'https://en.wikipedia.org/wiki/2022_Russian_invasion_of_Ukraine'
fhand = urllib.request.urlopen(link)
count = 0
for line in fhand:
    char = line.decode().split()
    print(char)
