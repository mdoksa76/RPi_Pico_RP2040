import machine
import time
import gc

def memtest(start_addr, end_addr, chunk_size):
    gc.collect()
    allocated_memory_before = gc.mem_alloc() / 1024  # Convert to KB
    free_memory_before = gc.mem_free() / 1024  # Convert to KB
    print(f"Allocated memory before test: {allocated_memory_before:.2f} KB")
    print(f"Free memory before test: {free_memory_before:.2f} KB")

    start_time = time.ticks_ms()
    print("Starting memory test...")

    # Write pattern to memory
    for addr in range(start_addr, end_addr, chunk_size):
        machine.mem32[addr] = addr
        if addr % 0x1000 == 0:  # Print progress every 4KB
            print(f"Writing to address {hex(addr)}")
            time.sleep(0.01)  # Add a small delay to prevent overwhelming the microcontroller

    write_time = time.ticks_ms()
    print("Writing complete. Verifying pattern...")

    # Verify pattern
    for addr in range(start_addr, end_addr, chunk_size):
        if machine.mem32[addr] != addr:
            print(f"Memory test failed at address {hex(addr)}")
            return False
        if addr % 0x1000 == 0:  # Print progress every 4KB
            print(f"Verifying address {hex(addr)}")
            time.sleep(0.01)  # Add a small delay to prevent overwhelming the microcontroller

    end_time = time.ticks_ms()
    print("Memory test passed")

    # Print time details
    total_time = time.ticks_diff(end_time, start_time) / 1000
    write_duration = time.ticks_diff(write_time, start_time) / 1000
    verify_duration = time.ticks_diff(end_time, write_time) / 1000
    print(f"Total time: {total_time:.2f} seconds")
    print(f"Writing time: {write_duration:.2f} seconds")
    print(f"Verifying time: {verify_duration:.2f} seconds")

    gc.collect()
    allocated_memory_after = gc.mem_alloc() / 1024  # Convert to KB
    free_memory_after = gc.mem_free() / 1024  # Convert to KB
    print(f"Allocated memory after test: {allocated_memory_after:.2f} KB")
    print(f"Free memory after test: {free_memory_after:.2f} KB")

    return True

# Example usage
start_addr = 0x2000C800  # Start address of RAM (50 KB)
end_addr = 0x20039000    # End address of RAM (228 KB)
chunk_size = 4           # Chunk size (4 bytes)
memtest(start_addr, end_addr, chunk_size)
