fname = input('Enter the file name: ')
fhand = open(fname,'r')
count = 0
total = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        pos = line.find(':')
        s_num = line[pos+1:].lstrip()
        f_num = float(s_num)
        total = total + f_num
#print(total)
print('Average spam confidence:',total/count)
