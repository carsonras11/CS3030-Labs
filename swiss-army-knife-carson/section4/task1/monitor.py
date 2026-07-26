import psutil
import time
from datetime import datetime


while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    available_ram = ram.available / (1024 ** 3)

    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("CPU Usage:", cpu, "%")
    print("Available RAM:", round(available_ram, 2), "GB")
    print("Disk Usage:", disk.percent, "%")

    if cpu > 80 or available_ram < 1 or disk.percent > 90:
        print("\033[91mWARNING: System resources have passed a limit.\033[0m")

    print()
    time.sleep(60)
