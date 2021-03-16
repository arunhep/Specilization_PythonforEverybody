fname = input("Enter the file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)
count = 0
for line in fhand :
    line = line.rstrip()
    if line.startswith('From:') : continue
    if line.startswith('From') :
        count = count + 1
        flist = line.split()
        print(flist[1])
print("There were", count, "lines in the file with From as the first word")
