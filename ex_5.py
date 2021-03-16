#assignment 5
#def is the key word for the definition of function with : at the end
#break -> out of the loop
#continue -> get to next iteration (not out of loop)
'''
for i in [5,4,3,2,1] :
    print(i)
print('Blastoff!')

friends = ['Arun','Nishu','Vivaan']
for friend in friends :
    print('Happy New Year',friend)
print('Blastoff!')

largest_so_far = None
print('Before', largest_so_far)
for the_num in [9,23,45,57,35,12,43] :
    if largest_so_far is None :
        largest_so_far = the_num
    elif the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After',largest_so_far)
'''
tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)
