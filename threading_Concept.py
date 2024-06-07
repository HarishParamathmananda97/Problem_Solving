import threading
import time 
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Function to calculate square of a number
def calculate_square(num):
    # Simulating a delay to demonstrate I/O - bound task
    time.sleep(1)
    print("Time now is: ", time.time())
    return num * num



# Using Threading directly
start_time = time.time()
threads = []
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    thread = threading.Thread(target = lambda: print(f"Square of {num}: {calculate_square(num)}"))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Time taken using threading: ", time.time() - start_time)

# Using ThreadPoolExecutor from concurrent.futures
start_time = time.time()
with ThreadPoolExecutor() as executor:
    results = executor.map(lambda num: (num, calculate_square(num)), numbers)

for num, result in results:
    print(f"Square of {num}: {result}")

print("Time taken using ThreadPoolExecutor: ", time.time() - start_time)