lister = [12 , 3, 5, 4 , 1, 9]
for i in range(1 , len(lister)):
    key = lister[i]
    j = i-1
    while j>= 0 and lister[j] < key:
        lister[j+1] = lister[j]
        j = j-1
        lister[j+1] = key

