#assignment 3.3
s_hrs = input('Enter the score : ')
try :
    f_hrs = float(s_hrs)
except :
    print('Error, give the numerical value')
    quit()
if f_hrs > 1.0 :
    print ('Value is out of range, provide number between 0.0 and 1.0')
    quit()
elif f_hrs < 0.0 :
    print ('Value is out of range, provide number between 0.0 and 1.0')
    quit()

if f_hrs >= 0.9 :
    print('A')
elif f_hrs >= 0.8 :
    print('B')
elif f_hrs >= 0.7 :
    print('C')
elif f_hrs >= 0.6 :
    print('D')
elif f_hrs < 0.6 :
    print('F')
