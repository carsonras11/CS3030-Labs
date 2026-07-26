def read_log(file_name):
    # gives back one line at a time and uses less memory when dealing with a huge file. f.read() loads the whole file at once, which can be scary with large files.

    with open(file_name, "r") as file:
        for line in file:
            yield line


for line in read_log("../task1/sample.log"):
    if "CRITICAL" in line:
        print(line.strip())
