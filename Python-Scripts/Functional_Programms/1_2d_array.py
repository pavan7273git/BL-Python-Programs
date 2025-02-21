'''1. 2D Array
a. Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.
b. I/P -> M rows, N Cols, and M * N inputs for 2D Array. Use Java Scanner Class
c. Logic -> create 2 dimensional array in memory to read in M rows and N cols
d. O/P -> Print function to print 2 Dimensional Array. In Java use PrintWriter with
OutputStreamWriter to print the output to the screen. '''

def read_2d_array(rows, column):
    array = []
    
    
    print(f"Enter {rows * column} elements for the 2D array:")
    for i in range(rows):
        row = []
        for j in range(column):
            row.append(int(input(f"Element at position ({i+1},{j+1}): ")))  
        array.append(row)
    
    return array


def print_2d_array(array):
    print("The 2D array is:")
    for row in array:
        print(" ".join(map(str, row)))  


M = int(input("Enter the number of rows (rows): "))
N = int(input("Enter the number of columns (column): "))


array = read_2d_array(M, N)

print_2d_array(array)