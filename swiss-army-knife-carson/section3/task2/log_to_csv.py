import re
import csv


log_file = open("../task1/sample.log", "r")
lines = log_file.readlines()
log_file.close()


csv_file = open("error_report.csv", "w", newline="")
writer = csv.writer(csv_file)


writer.writerow(["Date", "Error Type", "Message"])


for line in lines:
    if "Error" in line:
        pattern = r"\[(\d{4}-\d{2}-\d{2}) \d{2}:\d{2}\] Error ([A-Z]+): (.+)"

        match = re.search(pattern, line)

        if match:
            date = match.group(1)
            error_type = match.group(2)
            message = match.group(3)

            writer.writerow([date, error_type, message])


csv_file.close()


print("error_report.csv was created.")
