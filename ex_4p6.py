#assignment 4.6
#def is the key word for the definition of function with : at the end

s_hrs = input('Enter the hours :')
s_rate = input('Enter the rate per hour :')
f_hrs = float(s_hrs)
f_rate = float(s_rate)

def computepay(hrs,rate) :
    if hrs > 40 :
        pay = 40 * rate
        otp = (hrs - 40) * rate * 1.5
        grosspay = pay + otp
    elif hrs < 40 :
        grosspay = hrs * rate
    return grosspay

print('Pay',computepay(f_hrs,f_rate))
