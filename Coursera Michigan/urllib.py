import urllib

link = input('Enter the link: ')
fhand = urllib.request.urlopen(link)

for line in fhand :
    print(line)