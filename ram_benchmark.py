import gc
import time

def memory_benchmark():
    gc.collect()
    initial_free = gc.mem_free()
    print("Initial free memory: {} bytes".format(initial_free))

    # Allocate memory in smaller blocks
    allocations = []
    block_size = 128  # Allocate 128 bytes at a time
    num_blocks = 500  # Number of blocks to allocate
    start_time = time.ticks_us()
    for i in range(num_blocks):
        try:
            allocations.append(bytearray(block_size))
        except MemoryError:
            print("Memory allocation failed at block {}".format(i))
            break
    end_time = time.ticks_us()
    elapsed_time = time.ticks_diff(end_time, start_time) / 1000000

    gc.collect()
    final_free = gc.mem_free()
    print("Final free memory: {} bytes".format(final_free))
    print("Memory allocated: {} bytes".format(initial_free - final_free))
    print("Elapsed time for allocation: {:.6f} seconds".format(elapsed_time))

    # Deallocate memory
    start_time = time.ticks_us()
    allocations = None
    gc.collect()
    end_time = time.ticks_us()
    elapsed_time = time.ticks_diff(end_time, start_time) / 1000000

    gc.collect()
    final_free = gc.mem_free()
    print("Free memory after deallocation: {} bytes".format(final_free))
    print("Elapsed time for deallocation: {:.6f} seconds".format(elapsed_time))

memory_benchmark()
