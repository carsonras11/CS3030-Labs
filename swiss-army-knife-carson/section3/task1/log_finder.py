import re

file = open("sample.log", "r")
text = file.read()
file.close()

ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}"
time_pattern = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}\]"

ip_addresses = re.findall(ip_pattern, text)
timestamps = re.findall(time_pattern, text)

print("IP Addresses:")

for ip in ip_addresses:
	print(ip)

print("Timestamps:")

for time in timestamps:
	print(time)
