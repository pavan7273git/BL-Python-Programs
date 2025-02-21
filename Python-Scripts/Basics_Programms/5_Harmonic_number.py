'''5. Harmonic Number
a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
(http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
b. I/P -> The Harmonic Value N. Ensure N != 0
c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
d. O/P -> Print the Nth Harmonic Value.'''

#number=int(input('Enter the number :'))

'''
#while True:
if number == 0 :
    print('Number should be greater than zero ')
    exit()
elif number>0 :
    sum=0
    for i in range(1,number + 1):
        sum += 1/i
print(f'The {number}th Harmonic Number is: {sum}')

'''

while True:
    number=int(input('Enter the number :'))
    if number>0:
        sum=0
        for i in range(1,number+1):
            sum+=1/i
        print(f'The {number}th Harmonic Number is: {sum : .2f}')
        break

    else:
        print(f'The Number should be Greater Than Zero, Enter Number again :')
       
    

