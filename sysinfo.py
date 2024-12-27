import machine
import utime
import time
import os
import sys
import gc

# Get the platform
platform = sys.platform
print("Platform:", platform)

# Get the unique ID of the Pico
unique_id = machine.unique_id()
formatted_id = ''.join('{:02x}'.format(x) for x in unique_id)
#print("Unique ID:", unique_id)
print("Unique ID:", formatted_id)

# Get the frequency of the CPU
cpu_freq = machine.freq()/1e6
print("CPU Frequency:", cpu_freq, "MHz")

# Force a garbage collection cycle
gc.collect()

# Print the amount of memory allocated and free
print("Allocated memory: {:.2f} kbytes".format(gc.mem_alloc() / 1024))
print("Free memory: {:.2f} kbytes".format(gc.mem_free() / 1024))

# Set a new garbage collection threshold
gc.threshold(50000)

# Print the current garbage collection threshold
print("GC threshold:", gc.threshold())

# Get the file system statistics
stat = os.statvfs('/')

# Calculate the total, used, and free space in bytes
total = stat[1] * stat[2]
free = stat[0] * stat[3]
used = total - free

# Convert bytes to megabytes
MB = 1024 * 1024
total_MB = total / MB
used_MB = used / MB
free_MB = free / MB

# Print the results in megabytes
print("Total storage: {:.2f} MB".format(total_MB))
print("Used storage: {:.2f} MB".format(used_MB))
print("Free storage: {:.2f} MB".format(free_MB))

# Get the reset cause
reset_cause = machine.reset_cause()
print("Reset Cause:", reset_cause)

# Get the current time in seconds since the epoch
current_time = utime.time()
print("Current time (seconds since epoch):", current_time)
calendar_time = utime.localtime()
year = calendar_time[0]
month = calendar_time[1]
day = calendar_time[2]
hour = calendar_time[3]
minute = calendar_time[4]
print("Current time:", calendar_time)
formatted_date = "{:02d}-{:02d}-{:04d} {:02d}:{:02d}".format(day, month, year, hour, minute)
print("Current date (D-M-Y HH:MM):", formatted_date)

# Get the uptime in milliseconds since boot
uptime_ms = utime.ticks_ms()
print("Uptime (ms):", uptime_ms)

# Get the uptime in seconds since boot
uptime_s = utime.ticks_ms() // 1000
print("Uptime (s):", uptime_s)
uptime_hours = uptime_ms / (1000 * 60 * 60)
print("Uptime (hours):", uptime_hours)

# Get the current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# List files in the current directory
files = os.listdir()
print(f"Files in {cwd}: {files}")

# Get the version of MicroPython
version = sys.version
print("MicroPython version:", version)
