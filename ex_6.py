'''
fruit = 'banana'
count = 0
for letter in fruit :
    if letter == 'a' :
        count = count + 1
print(count)
print(len(fruit))
s = 'Monty Python'
print(s[0:4])
'''
#colon operator to define the range. up to but not including last digit

x = 'From marquard@uct.ac.za'
print(x.find('uct'))
#print(x[8])

#print(len('banana')*7)


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

greet = 'Hello Bob'
print(greet.upper())
