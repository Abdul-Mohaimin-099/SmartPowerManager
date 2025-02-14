import os

# Specify the full path to the .ico file
icon_path = r"D:\Projects\Smart Power Manager\app_icon.ico"

# Check if the file exists and print the result
if os.path.exists(icon_path):
    print(f"File found: {icon_path}")
else:
    print(f"File not found: {icon_path}")
