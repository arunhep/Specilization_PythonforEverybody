counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names :
    counts[name] = counts.get(name,0) + 1
#    if name not in counts:
    #    counts[name] = 1
#    else :
#        counts[name] = counts[name] + 1
print(counts)

stuff = dict()
print(stuff.get('candy',-1))
