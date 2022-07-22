import os
from threading import Thread 

from cryptography.fernet import Fernet, InvalidToken


while True:
    if(input("Please enter the password:" ) == "genius jimam"):
        break
    print("Password was not correct")


KEY = input('Please enter the key: ')

fernet = Fernet(KEY)                                                                    

def decrypt(file):
    try: 
        with open(file, "rb") as myFile:
            myFileData = myFile.read()

        decryptedMyFileData = fernet.decrypt(myFileData)

        with open(file, "wb") as myFile:
            myFile.write(decryptedMyFileData)
        
        print(file, ", decrypted")
    except InvalidToken:
        print('Invalid Key')
 

    except Exception as e:
        print(e)


 
def run():   
    for root, folders, files in os.walk("U:\\"):
        for file in files:
            decrypt(os.path.join(root, file))
            

Thread(target=run).start()
    

 
# for file in os.listdir():
#     if file in ['encrypt.py', 'key_file.key', "decrypt.py"]:
#         continue
#     elif os.path.isfile(file):
#         decrypt(file)