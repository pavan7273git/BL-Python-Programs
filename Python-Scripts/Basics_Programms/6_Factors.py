'''6. Factors
a. Desc -> Computes the prime factorization of N using brute force.
b. I/P -> Number to find the prime factors
c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
d. O/P -> Print the prime factors of number N.'''

number = int(input("Enter a number to find its prime factors: "))

if number <= 1:
    print("Please enter a number greater than 1.")
else:
    print("Prime factors of", number, "are:")

    
    while number % 2 == 0:
        print(2, end=" ")
        number = number // 2

    
    i = 3
    while i * i <= number:
        while number % i == 0:
            print(i, end=" ")
            number = number // i
        i += 2

    
    if number > 2:
        print(number)