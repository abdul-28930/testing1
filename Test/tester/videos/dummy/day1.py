import threading
import time
import tracemalloc

def sleep_sort(arr):
    def sleep_and_print(n):
        time.sleep(n)
        print(n, end=' ')

    threads = []
    for num in arr:
        thread = threading.Thread(target=sleep_and_print, args=(num,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

arr = [3, 1, 4, 1, 5, 9, 2]

# Start time measurement
start_time = time.time()
print("Original array:", arr)
print("Sorted array:", end=' ')
sleep_sort(arr)
end_time = time.time()

print("\nTime taken:", end_time - start_time, "seconds")

# Start memory tracking
tracemalloc.start()

# Capture current memory usage
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("\nMemory usage:")
print(f"Current size: {current / 1024:.2f} KB")
print(f"Peak size: {peak / 1024:.2f} KB")
