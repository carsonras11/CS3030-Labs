import os
import shutil
import logging

# audit
logging.basicConfig(
    filename="defensive_script.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

config_file = "config.txt"
backup_file = "config_backup.txt"

# file limit
max_size = 1024

try:
    logging.info("script started")

    # secret
    secret = os.getenv("BACKUP_API_KEY")

    if secret == None:
        raise ValueError("secret is missing")

    # check file
    if os.path.exists(config_file) == False:
        raise FileNotFoundError("config.txt was not found")

    size = os.path.getsize(config_file)

    if size > max_size:
        raise ValueError("config.txt is too large")

    # backup
    shutil.copy(config_file, backup_file)

except FileNotFoundError as error:
    print("Error:", error)
    logging.error(error)

except PermissionError:
    print("Permission denied")
    logging.error("permission denied")

except ValueError as error:
    print("Error:", error)
    logging.warning(error)

except Exception as error:
    print("Something else went wrong:", error)
    logging.error(error)

else:
    print("Backup made")
    logging.info("backup made")

finally:
    print("Done")
    logging.info("script finished")
