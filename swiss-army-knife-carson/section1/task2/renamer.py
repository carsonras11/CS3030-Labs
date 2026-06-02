import os

folder = "task2_data"
number = 1

for file_name in os.listdir(folder):
    old_file = folder + "/" + file_name
    new_file = folder + "/Hawaii_Trip_" + str(number) + ".jpg"

    os.rename(old_file, new_file)

    number = number + 1
