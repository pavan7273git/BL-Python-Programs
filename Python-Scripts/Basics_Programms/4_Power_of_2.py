'''
4. Power of 2
a. Desc -> This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N.
b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
c. Logic -> repeat until i equals N.
d. O/P -> Print the year is a Leap Year or not.'''



while True:
    power_of_n=int(input('Enter the Power of N: '))
    if 0 <= power_of_n < 31 :
        for i in range(power_of_n + 1):
            print(f'The Value of 2 power {i} is: {2 ** i}')
        break

    else:
            print('The Power Should be in range 0 to 31,Enter the Power again :')
      