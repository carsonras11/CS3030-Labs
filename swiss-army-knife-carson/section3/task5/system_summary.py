import subprocess
import re

result = subprocess.run(["who"], capture_output=True, text=True)

pattern = r"(\S+)\s+(\S+)\s+(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2})"

print(f"{'USER':<15}{'TERMINAL':<15}{'DATE':<15}{'TIME'}")

for line in result.stdout.splitlines():
    match = re.search(pattern, line)

    if match:
        print(f"{match.group(1):<15}{match.group(2):<15}{match.group(3):<15}{match.group(4)}")
