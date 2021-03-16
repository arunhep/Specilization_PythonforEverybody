text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0.8475')
#print(pos)
s_num = (text[pos:pos+6])
f_num = float(s_num)
print(f_num)
