'''2. Sum of three Integer adds to ZERO
a. Desc -> A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0.
b. I/P -> N number of integer, and N integer input array
c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
d. O/P -> One Output is number of distinct triplets as well as the second output is to
print the distinct triplets.'''

def find_triplets(arr, N):
    triplets = []
    count = 0
    
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplet = sorted([arr[i], arr[j], arr[k]])
                    if triplet not in triplets:
                        triplets.append(triplet)
                        count += 1
    
    return count, triplets


N = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the integers separated by space: ").split()))


count, triplets = find_triplets(arr, N)
print("Number of distinct triplets:", count)
print("Distinct triplets:",triplets)