import machine

def check_memory(start_addr, end_addr, chunk_size):
    print(f"Checking memory from {hex(start_addr)} to {hex(end_addr)}:")
    
    for addr in range(start_addr, end_addr, chunk_size):
        value = machine.mem32[addr]
        print(f"Address {hex(addr)}: {hex(value)}")

# Example usage
start_addr = 0x20000000  # Start address of RAM (0 KB)
end_addr = 0x20039000    # End address of RAM (228 KB)
chunk_size = 1024        # Chunk size (1024 bytes)
check_memory(start_addr, end_addr, chunk_size)
