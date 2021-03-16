fname = input('Enter the file name: ')
fhand = open(fname,'r')
for line in fhand:
    n_line = line.rstrip()
    print(n_line.upper())
