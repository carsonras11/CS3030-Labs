try:
    file = open("config.txt", "r")
    data = file.read()
    file.close()

    data = data.replace("status=active", "status=maintenance")

    file = open("config.txt", "w")
    file.write(data)
    file.close()

    print("Configuration updated.")

except FileNotFoundError:
    print("Error: The configuration file was not found.")

except PermissionError:
    print("Error: You do not have permission to access the file.")

except Exception as error:
    print("Error:", error)

finally:
    print("Operation Attempted")
