import re
fh = open('regex_sum_939028.txt','r')
sum = 0
for line in fh :
    x = re.findall('[0-9]+',line)
    if len(x) < 1 : continue
    for i in x :
        sum = sum + int(i)
print(sum)



#line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#x = re.findall('\S+?@\S+',line)
#print(x)

#x = 'From: Using the : character'
#y = re.findall('^F.+:', x)
#print(y)


'''
fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
#bigcount = None
#bigword = None
for line in fh :
    line = line.rstrip()
    if line.startswith('From:') : continue
    if line.startswith('From'):
        flist = line.split()
        flist_new = flist[5].split(':')
        counts[flist_new[0]] = counts.get(flist_new[0],0) + 1
#print(sorted(counts.items()))
for h,c in sorted(counts.items()) :
    print(h,c)
    #if bigcount is None or count > bigcount:
    #    bigword = word
    #    bigcount = count
#print(bigword, bigcount)
'''
