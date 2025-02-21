'''3. Leap Year
a. I/P -> Year, ensure it is a 4 digit number.
b. Logic -> Determine if it is a Leap Year.
c. O/P -> Print the year is a Leap Year or not.'''

#Taking the input from user

year=int(input('Enter the Year: '))
while True:
    #for integer values we cant take the length
    #so we convert the integer to string using str function
    if len(str(year)) == 4:
        if(year % 4 == 0 and year % 100 != 0)or (year % 400 == 0 ):
            print(f'The Entered Year {year} is Leap Year')
            break

        else:
            print(f'The Entered Year {year} is Not a Leap Year')
            break


    #if the year do not have length 4 then we will take input again
    else:
        print('The Year Should contain 4 digits')
        year=int(input('Enter the Year again! : '))
