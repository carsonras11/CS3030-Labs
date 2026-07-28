import shutil

shutil.copytree("demo_files", "demo_backup")
print("Folder copied successfully.")

shutil.make_archive("demo_backup", "zip", "demo_backup")
print("ZIP archive created successfully.")
