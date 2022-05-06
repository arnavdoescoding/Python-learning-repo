def merging(inpa):
    size = len(inpa)
    if size > 1:
        mid = size // 2
        lef = inpa[:mid]
        rig = inpa[mid:]

        merging(lef)
        merging(rig)
        p = 0
        q = 0
        r = 0
        lefts = len(lef)
        rigs = len(rig)
        while p < lefts and q < rigs:
            if lef[p] < rig[q]:
                inpa[r] = lef[p]
                p+=1
            else:
                inpa[r] = rig[q]
                q+=1
            r+=1 
        while p< lefts:
            inpa[r] = lef[p]
            p+=1
            r+=1
        while q< rigs:
            inpa[r] = rig[q]
            q+=1
            r+=1


inp = [23, 1 , 45 , 2 , 0]
merging(inp)
print(inp)



