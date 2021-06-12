#   PURPOSE - This program is for encrypting and decrypting data using customizable encryption options
#       -Encryption is done using a cipher, which can be broken up into multiple files
#       -Every user's cipher is different
#       -Users can create their own ciphers manually, or have CustomEncryptor generate them automatically at random

#   To further increase the efficacy of this program, you can change the function names to obscure their purpose in your other code.
#   For Ctrl+H purposes, here is a list of all the functions and important variables that you may want to use in other programs:
#       CustomEncryptor - the class name
#       CipherLocations - the name of the .txt containing your cipher file locations
#       cipher_file - the variable assigned to the .txt containing your cipher file locations
#       cipher_locations - the list of your cipher locations
#       cipher - the cipher
#       fetchData - function that attempts to open a file given a location
#       encrypt - function that encrypts data or a file
#       decrypt - function that decrypts data or a file
#       generateCipher - function for creating a brand new cipher

import pickle
import random

from FetchEncryptedFiles import FetchEncryptedFiles
from SortDictionary import SortDictionary

class CustomEncryptor:
    def __init__(self):
    # This is for sorting the cipher, which is optional; set self.sort to True if you want the cipher to be more readable
        self.sort = True
    # byte_length determines how many characters each character is encrypted to. 4 is the default
        self.byte_length = 4
    # Create a .txt file with the locations of your cipher files on each line. cipher_file will be assigned to that file
        cipher_file = open('Vault - Home.txt', 'r')
        cipher_locations = []
        for line in cipher_file:
            cipher_locations.append(line.split('\n')[0])
    # The following for loop assembles the cipher from the various cipher files
        self.cipher = {}
        for location in cipher_locations:
            try:
                file_data_dict = pickle.load(open(location, 'rb'))
            except:  
                try:
                    raw_file_data_dict = open(location, 'r')
                except:
                    #try:
                        FEF = FetchEncryptedFiles()
                        raw_file_data_dict = FEF.fetchFile({'File Name': location})
                        if type(raw_file_data_dict) == bytes:
                            raw_file_data_dict = str(raw_file_data_dict).split("'")[1].split('\\r\\n')
                        del FEF
                    #except:
                    #    print('ERROR! Failed to locate file at ' + location)
                file_data_dict = {}
                line_count = 0
                last_line = False
            # The following for loop removes stray characters from text format files or encrypted files
                for line in raw_file_data_dict:
                    if '\n' in str(line):
                        line = str(line).split('\n')[0]
                    line_count += 1
                    if line_count % 2 == 0:
                        file_data_dict[last_line] = line
                    last_line = line
            for char in file_data_dict:
                if str(file_data_dict[char]) != '':
                    self.cipher[str(char)] = str(file_data_dict[char])
    # Sorts the self.cipher dict for easier reading. This is optional and purely for double-checking purposes
        if self.sort:
            SD = SortDictionary()
            self.cipher = SD.sortDictByKey(self.cipher)
            del SD
    # Creates an inverted self.cipher dict with the keys and values switched; this is used in the decrypt() function
        self.cipher_inverse = {value: key for key, value in self.cipher.items()}
             
# This function is for quickly opening files in the case that encrypt() or decrypt() is sent a file location rather than data for encryption
    def fetchData(self, location):
        try:
            data = list(open(location, 'r'))
        except:
            data = open(location, 'r')
        print(data)
        return(data)
            
#   This function encrypts data using self.cipher
    def encrypt(self, file_info):
        try:
            data = self.fetchData(file_info)
        except:
            data = file_info
        if type(data) == str:
            output = ''
            for char in data:
                output += self.cipher[char]
        # Random extra characters are added to the end of the encryption so that all encryptions are the same length
            while len(output) < 100 * self.byte_length:
                output += random.choice(list(self.cipher_inverse))
        else:
            output = []
            for line in data:
                line_output = ''
                for char in line:
                    line_output += self.cipher[char]
            # Random extra characters are added to the end of the encryption so that all encryptions are the same length
                while len(line_output) < 100 * self.byte_length:
                    line_output += random.choice(list(self.cipher_inverse))
                output.append(line_output)
        return(output)

#   This function decrypts data using self.cipher_inverse
    def decrypt(self, file_info):
        try:
            data = self.fetchData(file_info)
        except:
            data = file_info
        if type(data) == str:
            output = ''
            byte = ''
            for char in data:
                byte += char
                if len(byte) == self.byte_length:
                    output += self.cipher_inverse[byte]
                    byte = ''
        else:
            output = []
            for line in data:
                line_output = ''
                byte = ''
                for char in line:
                    byte += char
                    if len(byte) == self.byte_length:
                        line_output += self.cipher_inverse[char]
                        byte = ''
                output.append(line_output)
        return(output)

#   This function is for generating a new cipher
#   Cipher generation can be done manually, allowing you to choose what each character is assigned to
#   Cipher generation can also be done automatically, in which case it will generate a cipher for you at random
    def generateCipher(self):
        blank_cipher = {'0': '', '1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': '', \
                        'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': '', 'h': '', 'i': '', 'j': '', 'k': '', 'l': '', 'm': '', \
                        'n': '', 'o': '', 'p': '', 'q': '', 'r': '', 's': '', 't': '', 'u': '', 'v': '', 'w': '', 'x': '', 'y': '', 'z': '', \
                        'A': '', 'B': '', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '', 'H': '', 'I': '', 'J': '', 'K': '', 'L': '', 'M': '', \
                        'N': '', 'O': '', 'P': '', 'Q': '', 'R': '', 'S': '', 'T': '', 'U': '', 'V': '', 'W': '', 'X': '', 'Y': '', 'Z': '', \
                        '-': '', '.': '', ',': '', ' ': '', '!': '', '?': '', '/': '', '@': '', '^': '', '*': '', '(': '', ')': ''}
        gear = False
    # Choose automatic or manual generation of cipher in this while loop
        while not(gear):
            gear = str(input('Would you like to manually generate a cipher, or have them made automatically?\n(1) : Manual\n(2) : Automatic\n\nGear : '))
            if gear.lower() == 'manual' or gear == '1':
                gear = 'manual'
            elif gear.lower() == 'automatic' or gear.lower() == 'auto' or gear == '2':
                gear = 'automatic'
            else:
                gear = False
                print('That input was invalid! Please try again.')
        new_cipher = {}
        new_cipher_inverse = {}
        character_count = 0
    # This for loop takes the user through every encryptable character, allowing them to assign each character to a combination of numbers of their choice
        if gear == 'manual':
            print('OK! Please input a ' + str(self.byte_length) + '-digit value to assign to each of the following ' + str(len(blank_cipher))+ ' characters:')
            for char in blank_cipher:
                character_count += 1
                print('Character #' + str(character_count))
                new_value = False
                while not(new_value):
                    new_value = str(input(char + ' -> '))
                    if not(new_value.isnumeric()) or len(new_value) != self.byte_length:
                        print("Whoops! That is not a valid value for character assignment. Please try again.")
                        new_value = False
                    elif new_value in new_cipher_inverse:
                        print("Whoops! That value has already been used for " + new_cipher_inverse[new_value] + ". Please try again.")
                        new_value = False
                new_cipher[char] = new_value
                new_cipher_inverse[new_value] = char
    # This for loop runs through all of the encryptable characters and assigns each one to a random number of the appropriate length
        elif gear == 'automatic':
            print('OK! The cipher will be generated automatically for you.')
            for char in blank_cipher:
                character_count += 1
                print('Character #' + str(character_count))
                new_value = False
                while not(new_value):
                    new_value = str(int(random.random() * 10000))
                # This if corrects the rare case where random.random() returns 1
                    if len(new_value) > self.byte_length:
                        new_value = '0000'
                # This while corrects the case where random.random() returns a value below .1
                    while len(new_value) < self.byte_length:
                        new_value = '0' + new_value
                # This if rerolls the new_value if it is a duplicate and has already been used
                    if new_value in new_cipher_inverse:
                        new_value = False
                new_cipher[char] = new_value
                new_cipher_inverse[new_value] = char
                print(char + ' -> ' + new_value)
        return(new_cipher)
                
        
