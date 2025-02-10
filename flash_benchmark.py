import time

def flash_benchmark():
    # Create a test file
    file_size = 1024 * 1024  # 1MB
    data = bytearray(1024)  # 1KB of data

    # Write benchmark
    start_time = time.ticks_us()
    with open("test_file.bin", "wb") as f:
        for _ in range(file_size // len(data)):
            f.write(data)
    end_time = time.ticks_us()
    write_time = time.ticks_diff(end_time, start_time) / 1000000
    print("Write time: {:.6f} seconds".format(write_time))

    # Read benchmark
    start_time = time.ticks_us()
    with open("test_file.bin", "rb") as f:
        while f.read(len(data)):
            pass
    end_time = time.ticks_us()
    read_time = time.ticks_diff(end_time, start_time) / 1000000
    print("Read time: {:.6f} seconds".format(read_time))

    # Delete the test file
    import os
    os.remove("test_file.bin")

flash_benchmark()
