import os
from win32api import GetLogicalDriveStrings

drives = GetLogicalDriveStrings().split("\x00")
drives.pop()

for drive in drives:
    if(drive == "C:\\"):
        continue
    for root, folders, files in os.walk(drive):
        for file in files:
            print(os.path.join(root, file))