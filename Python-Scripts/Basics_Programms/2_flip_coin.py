'''2. Flip Coin and print percentage of Heads and Tails
a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.
b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
heads
c. O/P -> Percentage of Head vs Tails'''



import random

#Taking input from user
n_times=int(input("Enter number to flip coin: "))
head=0
tail=0

if n_times <= 0:
    print('The Number should be greater than zero')
    exit()

else:
    for _ in range(n_times):
     if random.random() < 0.5:
       tail+=1
     else:
        head+=1

head_percentage=(head/n_times)*100
tail_percentage=(tail/n_times)*100

#printing the output in percentage format
print(f"The Head percentage in {n_times} flips is: ({head_percentage : .2f}%)")
print(f"The Tail percentage in {n_times} flips is: ({tail_percentage :.2f}%)")

     
    
