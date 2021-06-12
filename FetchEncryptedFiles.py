#   PURPOSE - This is a simple program for retrieving encrypted files on a flash drive or other removable storage

import pickle
import zipfile

class FetchEncryptedFiles:

#   This function retrieves the desired file from the locked zipfile
    def fetchFile(self, *args):
        try:
            file_name = args[0]['File Name']
        except:
            file_name = str(input('What is the name of the file you are trying to access?\n    File Name: '))
        try:
            locked_zip_name = args[0]['Locked Zip Name']
        except:
            locked_zip_name = str(input('What is the name of the encrypted zip file?\n    Zip File Name: '))
        try:
            key_name = args[0]['Key Name']
        except:
            key_name = str(input('What is the name of the file for unlocking the encrypted zip file?\n    Key File Name: '))
        drive_list = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
        locked_file = False
        for drive in drive_list:
            if not(locked_file):
                try:
                    locked_file = zipfile.ZipFile(drive + ':/' + locked_zip_name, 'r')
                except:
                    print('File not found on ' + drive + ' drive. Moving on...')
        file = locked_file.read(file_name, pwd=bytes(self.fetchKey(key_name), 'UTF-8'))
        return(file)
    
#   This function retrieves the password necessary to open the locked zipfile
    def fetchKey(self, key_name):
        key = pickle.load(open(key_name, 'rb'))
        return(key)

