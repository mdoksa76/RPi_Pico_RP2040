import os

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
