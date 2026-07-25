import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
	description="Search a directory for files with a specific extension."
)

parser.add_argument("--path", required=True)
parser.add_argument("--ext", required=True)

args = parser.parse_args()

for file in Path(args.path).rglob(f"*{args.ext}"):
	print(f"Found file: {file}")
