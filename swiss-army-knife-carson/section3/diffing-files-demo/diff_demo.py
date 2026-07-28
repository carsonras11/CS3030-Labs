import difflib

with open("original_config.txt") as original:
    original_lines = original.readlines()

with open("current_config.txt") as current:
    current_lines = current.readlines()

differences = difflib.unified_diff(
    original_lines,
    current_lines,
    fromfile="Original Config",
    tofile="Current Config"
)

differences = list(differences)

if differences:
    print("The configuration file has been changed:")
    print("".join(differences))
else:
    print("No changes were found.")
