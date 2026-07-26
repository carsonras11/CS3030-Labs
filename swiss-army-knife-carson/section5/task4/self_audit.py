import os
import psutil


process = psutil.Process(os.getpid())

start_memory = process.memory_info().rss / (1024 ** 2)
start_cpu = process.cpu_times().user

print("Starting Memory:", round(start_memory, 2), "MB")
print("Starting CPU Time:", round(start_cpu, 2), "seconds")


numbers = list(range(5000000))


end_memory = process.memory_info().rss / (1024 ** 2)
end_cpu = process.cpu_times().user

memory_used = end_memory - start_memory
cpu_used = end_cpu - start_cpu

print("Ending Memory:", round(end_memory, 2), "MB")
print("Memory Used:", round(memory_used, 2), "MB")
print("CPU Time Used:", round(cpu_used, 2), "seconds")

# Memory Peak observed during testing: 203.89 MB
