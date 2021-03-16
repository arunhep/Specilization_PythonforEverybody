fname = input("Enter the file name: ")
fhand = open(fname)
lst = list()
for line in fhand :
    flist = line.split()
    for x in flist :
    #    print(x)
        if x not in lst :
            lst.append(x)
lst.sort()
print(lst)
