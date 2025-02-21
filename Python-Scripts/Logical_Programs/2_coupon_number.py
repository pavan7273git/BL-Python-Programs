'''2. Coupon Numbers
a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.
b. I/P -> N Distinct Coupon Number
c. Logic -> repeatedly choose a random number and check whether it's a new one.
d. O/P -> total random number needed to have all distinct numbers.
e. Functions => Write Class Static'''

import random

def generate_random_number(number):
    return random.randint(0, number - 1)

def collect_coupons(number):
    collected = set()
    total_random_numbers = 0
    
    while len(collected) < number:
        num = generate_random_number(number)
        collected.add(num)
        total_random_numbers += 1
    
    return total_random_numbers

def main():
    number = int(input("Enter number of distinct coupons: "))
    total_random_numbers = collect_coupons(number)
    print(f"Total random numbers needed to collect all {number} distinct coupons: {total_random_numbers}")

if __name__ == "__main__":
    main()
    
