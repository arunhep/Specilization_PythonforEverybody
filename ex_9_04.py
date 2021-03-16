fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
bigcount = None
bigword = None
for line in fh :
    line = line.rstrip()
    if line.startswith('From:') : continue
    if line.startswith('From'):
        flist = line.split()
        counts[flist[1]] = counts.get(flist[1],0) + 1
for word,count in counts.items() :
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
