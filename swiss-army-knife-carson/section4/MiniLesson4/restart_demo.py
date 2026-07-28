import time

print("The Python service started.", flush=True)

time.sleep(5)

print("The service is about to fail.", flush=True)

raise RuntimeError("Example failure")
