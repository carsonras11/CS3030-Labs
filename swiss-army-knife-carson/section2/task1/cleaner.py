from pathlib import Path

target_directory = '.'

for file_path in Path(target_directory).rglob("*.tmp"):
	print(f"Found junk: {file_path}")
