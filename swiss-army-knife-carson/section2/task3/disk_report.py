import subprocess

result = subprocess.run(["df", "-h"], capture_output=True, text=True)

for line in result.stdout.splitlines():
	if line.endswith(" /mnt/c"):
		print(line)
