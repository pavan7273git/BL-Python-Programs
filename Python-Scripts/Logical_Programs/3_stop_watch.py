'''3. Simulate Stopwatch Program
a. Desc -> Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks
b. I/P -> Start the Stopwatch and End the Stopwatch
c. Logic -> Measure the elapsed time between start and end
d. O/P -> Print the elapsed time.'''

import time

def start_stopwatch():
    input("Press Enter to start the stopwatch...")
    return time.time()

def stop_stopwatch():
    input("Press Enter to stop the stopwatch...")
    return time.time()

def calculate_elapsed_time(start_time, end_time):
    return end_time - start_time

def main():
    start_time = start_stopwatch()
    end_time = stop_stopwatch()
    elapsed_time = calculate_elapsed_time(start_time, end_time)
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
