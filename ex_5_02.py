largest = None
smallest = None
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
#    print(sval)
    try:
        fval = int(sval)
    except:
        print('Invalid input')
        continue

# to find the largest number
    if largest is None :
        largest = fval
    if fval > largest :
        largest = fval

# to fine the smallest number
    if smallest is None :
        smallest = fval
    if fval < smallest :
        smallest = fval

print('Maximum is',largest)
print('Minimum is',smallest)
