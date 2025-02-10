import time

# Get the frequency of the CPU
def cpu_speed():
    cpu_freq = machine.freq()/1e6
    print("CPU Frequency:", cpu_freq, "MHz")

def benchmark():
    start_time = time.ticks_us()
    iterations = 1000000
    result = 0
    for i in range(iterations):
        result += i * i
    end_time = time.ticks_us()
    elapsed_time = time.ticks_diff(end_time, start_time) / 1000000
    print("Elapsed time: {:.6f} seconds".format(elapsed_time))
    print("Iterations per second: {:.2f}".format(iterations / elapsed_time))

cpu_speed()
benchmark()
