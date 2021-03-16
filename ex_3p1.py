#assignment 3.1
s_hrs = input('Enter the hours : ')
f_hrs = float(s_hrs)
s_rate = input('Enter the rate : ')
f_rate = float(s_rate)
if f_hrs >  40 :
    pay = f_rate * f_hrs
    otp = (f_hrs - 40) * (f_rate * 0.5)
    totpay = pay + otp
else :
    totpay = f_rate * f_hrs

print(totpay)
