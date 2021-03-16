'''
print('My name is Arun and I am here to learn python')
x = 5
if x < 10 :
    print('Smaller')
if x > 20 :
    print('Bigger')
print('Finish')

n = 5
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff!')

jj = 23
kk = jj % 5
# % is the modulo operator
print(kk)

ll = (kk ** 2)
print(ll)


#order of evaluation
parenthses
exponentiation (power)
multiplication/division/remainder
addition/subtraction

if only one type of operation then go from left to right

#python knows the type of constant
eee = 'hello ' + 'there'
print(eee)

#we can instruct python to pause and read data from the user using the input() function
#the input() function returns a string
'''

#convert elevator floors
#inp = input('Europe floor?')
#usf = int(inp) + 1
#print('US floor', usf)

#x = 1 + 2 * 3 - 8 / 4
#print(x)

#hrs = input("Enter the hours :")
#rate = input("Enter rate per hour :")
#pay = float(hrs) * float(rate)
#print("pay:",pay)

# if statement ends with a : and next line is always indented
# 4 spaces indentation

#if x < 2 :
    #print('Below 2')
#elif x >= 2 :
#    print('medium')
#else :
#    print('large')
#print('All done')

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
    print(istr)
except:
    istr = -1
