#assignment 3.2
s_hrs = input('Enter the hours : ')
s_rate = input('Enter the rate : ')
try :
    f_hrs = float(s_hrs)
    f_rate = float(s_rate)
except :
    print('Error, give the numerical value')
    quit()
if f_hrs >  40 :
    pay = f_rate * f_hrs
    otp = (f_hrs - 40) * (f_rate * 0.5)
    totpay = pay + otp
else :
    totpay = f_rate * f_hrs

print(totpay)
