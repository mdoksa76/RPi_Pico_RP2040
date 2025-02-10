import gc

# Force a garbage collection cycle
gc.collect()

# Print the amount of memory allocated and free
print("Allocated memory:", gc.mem_alloc()/1024, "kbytes")
print("Free memory:", gc.mem_free()/1024, "kbytes")

# Set a new garbage collection threshold
gc.threshold(50000)

# Print the current garbage collection threshold
print("GC threshold:", gc.threshold())
