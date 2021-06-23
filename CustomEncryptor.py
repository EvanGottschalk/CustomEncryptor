#   PURPOSE - This program is for encrypting and decrypting data using customizable encryption options
#       -Encryption is done using a cipher, which can be broken up into multiple files
#       -Every user's cipher is different
#       -Users can create their own ciphers manually, or have CustomEncryptor generate them automatically at random

#   To further increase the efficacy of this program, you can change the function names to obscure their purpose in your other code.
#   For Ctrl+H purposes, here is a list of all the functions and important variables that you may want to use in other programs:
#       CustomEncryptor - the class name
#       CipherLocations - the name of the .txt containing your cipher file locations
#       cipher_file - the variable assigned to the .txt containing your cipher file locations
#       CP_locations_list - the list of your cipher locations
#       cipher - the cipher
#       fetchData - function that attempts to open a file given a location
#       encrypt - function that encrypts data or a file
#       decrypt - function that decrypts data or a file
#       generateCipher - function for creating a brand new cipher
#       byte_length - the number of digits characters are encrypted to

import pickle
import random

try:
    from FetchEncryptedFiles import FetchEncryptedFiles
    from SortDictionary import SortDictionary
except:
    from CustomEncryptor.FetchEncryptedFiles import FetchEncryptedFiles
    from CustomEncryptor.SortDictionary import SortDictionary

class CustomEncryptor:
    def __init__(self):
    # This is for sorting the cipher, which is optional; set self.sort to True if you want the cipher to be more readable
        self.sort = True
    # byte_length determines how many characters each character is encrypted to. 4 is the default
        self.byte_length = 4
    # encryption_length determines the maximum number of characters that can be encrypted
    # encryption_length determines the length that every encrypted piece of data will be
        self.encryption_length = 100

# This function reassembles the cipher used for encrypting and decrypting from the various Cipher Portion (CP) files
    def assembleCipher(self):
        print('OK! CustomEncryptor will now assemble your cipher.\n')
    # This while loop allows the user to choose between manually entering the CP file names, or accessing them from a file
        CP_location_mode = False
        while not(CP_location_mode):
            CP_location_mode = str(input('Would you like to input your Cipher Portion file names manually, or pull them from a file?\n(1) : Manual\n(2) : From File\n\nMode : '))
            if CP_location_mode.lower() == 'manual' or CP_location_mode == '1':
                CP_location_mode = 'manual'
            elif CP_location_mode.lower() == 'file' or CP_location_mode == '2':
                CP_location_mode = 'file'
            else:
                CP_location_mode = False
                print('That input was invalid! Please enter "1", "2", "manual" or "file".')
        CP_locations_list = []
    # Manual - this while loop allows the user to manually enter the CP file names
        if CP_location_mode == 'manual':
            collect_CP_file_names = True
            while collect_CP_file_names:
                CP_file_location = str(input('\nPlease enter the name of one of your Cipher Portion files. After entering them all, enter "done" or "0"\n    Cipher Portion File Name: '))
                if CP_file_location == '0' or CP_file_location.lower() == 'done':
                    print('OK! Your Cipher Portion file names have been collected. CustomEncryptor will now assemble your cipher from them.')
                    collect_CP_file_names = False
                else:
                    CP_locations_list.append(CP_file_location)
    # From File - this acquires the CP file names from a file
      # To use this mode, create a .txt file with the locations of your cipher files on each line. This can be done manually or with generateCipher()
      # CP_location_file will be assigned to that file
        elif CP_location_mode == 'file':
            CP_location_file = False
            while not(CP_location_file):
                try:
                    CP_location_file = str(input('\nWhat is the name of the file containing your Cipher Portion file names?\n    File Name: '))
                    CP_location_file = open(CP_location_file, 'r')
                except:
                    print('ERROR! Unabled to find file. Please try again.')
                    CP_location_file = False
            for line in CP_location_file:
                CP_locations_list.append(line.split('\n')[0])
    # The following for loop assembles the cipher from the various cipher files
        self.cipher = {}
        for location in CP_locations_list:
            try:
                CP_file = open(location, 'rb')
                file_data_dict = pickle.load(CP_file)
                CP_file.close()
            except:  
                try:
                    raw_file_data_dict = open(location, 'r')
                except:
                    try:
                        try:
                            FEF = FetchEncryptedFiles()
                        except:
                            FEF = FetchEncryptedFiles()
                        raw_file_data_dict = FEF.fetchFile({'File Name': location})
                        if type(raw_file_data_dict) == bytes:
                            raw_file_data_dict = str(raw_file_data_dict).split("'")[1].split('\\r\\n')
                        del FEF
                    except:
                        print('ERROR! Failed to locate file at ' + location)
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
            try:
                SD = SortDictionary()
            except:
                SD = SortDictionary
            self.cipher = SD.sortDictByKey(self.cipher)
            del SD
    # Creates an inverted self.cipher dict with the keys and values switched; this is used in the decrypt() function
        self.cipher_inverse = {value: key for key, value in self.cipher.items()}
        print('OK! Your cipher has been assembled.')
             
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
            while len(output) < self.encryption_length * self.byte_length:
                output += random.choice(list(self.cipher_inverse))
        else:
            output = []
            for line in data:
                line_output = ''
                for char in line:
                    line_output += self.cipher[char]
            # Random extra characters are added to the end of the encryption so that all encryptions are the same length
                while len(line_output) < self.encryption_length * self.byte_length:
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
                        '-': '', '.': '', ',': '', ' ': '', '!': '', '?': '', '/': '', '@': '', '^': '', '*': '', '(': '', ')': '', '_': ''}
        
   
        print('Welcome to the Cipher Generator! Please answer the following questions.\n')
        self.byte_length = False
    # This while loop allows users to choose the number of digits each encrypted character is after encryption
        while not(self.byte_length):
            self.byte_length = str(input('How many digits would you like your cipher to translate each character to?\n    Byte Length: '))
            try:
                self.byte_length = int(self.byte_length)
                if self.byte_length < len(str(len(blank_cipher))):
                    print('Invalid input! Byte Length must be at least ' + str(len(str(len(blank_cipher)))) + ' to prevent overlapping.')
                    self.byte_length = False
            except:
                print('Invalid input! Please enter an integer for the Byte Length.')
                self.byte_length = False
        print('OK! Byte Length of ' + str(self.byte_length) + ' has been chosen!\n')
    # Choose Gear - automatic or manual generation of cipher in this while loop
        gear = False
        while not(gear):
            gear = str(input('Would you like to manually generate a cipher, or have them made automatically?\n(1) : Manual\n(2) : Automatic\n\nGear : '))
            if gear.lower() == 'manual' or gear == '1':
                gear = 'manual'
            elif gear.lower() == 'automatic' or gear.lower() == 'auto' or gear == '2':
                gear = 'automatic'
            else:
                gear = False
                print('That input was invalid! Please enter "1", "2", or the name of a gear.')
        new_cipher = {}
        new_cipher_inverse = {}
        character_count = 0
    # Manual - This for loop takes the user through every encryptable character, allowing them to assign each character to a combination of numbers of their choice
        if gear == 'manual':
            print('OK! You have chosen to manually create your cipher.\n\nPlease input a ' + str(self.byte_length) + '-digit value to assign to each of the following ' + str(len(blank_cipher))+ ' characters:')
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
    # Automatic - This for loop runs through all of the encryptable characters and assigns each one to a random number of the appropriate length
        elif gear == 'automatic':
            print('OK! You have chosen to automatically create your cipher.\n\n The cipher will now be generated automatically at random.')
            for char in blank_cipher:
                character_count += 1
                print('Character #' + str(character_count))
                new_value = False
                while not(new_value):
                    new_value = str(int(random.random() * (10 ** self.byte_length)))
                # This if corrects the rare case where random.random() returns 1
                    if len(new_value) > self.byte_length:
                        new_value = '0' * self.byte_length
                # This while corrects the case where random.random() returns a value below .1
                    while len(new_value) < self.byte_length:
                        new_value = '0' + new_value
                # This if rerolls the new_value if it is a duplicate and has already been used
                    if new_value in new_cipher_inverse:
                        new_value = False
                new_cipher[char] = new_value
                new_cipher_inverse[new_value] = char
                print(char + ' -> ' + new_value)
        print('\nOK! Your cipher has been created. There are just a few more questions for you to answer.\n')
    # This while loop allows the user to choose into how many files their cipher will be broken up
        number_of_files = False
        while not(number_of_files):
            number_of_files = input('Into how many files would you like it to be divided?\n    Number of Files: ')
            try:
                number_of_files = int(number_of_files)
                if number_of_files < 1:
                    print('Invalid input! The number of files must be a positive integer.')
                    number_of_files = False
            except:
                print('Invalid input! The number of files must be a positive integer.')
                number_of_files = False
        if number_of_files == 1:
            print('OK! Your cipher will be stored entirely in 1 file. It will not be divided.\n')
        else:
            print('OK! Your cipher will be broken up into ' + str(number_of_files) + ' files.\n')
        # This while loop allows the user to choose between manually breaking up their cipher, or having it done automatically for them
            gear = False
            while not(gear):
                gear = str(input('Would you like to manually divide your cipher, or have it divided automatically?\n(1) : Manual\n(2) : Automatic\n\nGear : '))
                if gear.lower() == 'manual' or gear == '1':
                    gear = 'manual'
                elif gear.lower() == 'automatic' or gear.lower() == 'auto' or gear == '2':
                    gear = 'automatic'
                else:
                    gear = False
                    print('That input was invalid! Please enter "1", "2", or the name of a gear.')
            CP_file_name_list = []
        # Manual - This for loop allows the user to choose file names for their Cipher Portions, and to choose which characters are stored where
            if gear == 'manual':
                print('\nOK! You have chosen to manually divide your cipher. Please enter file names for each of your ' + str(number_of_files) + ' Cipher Portions.\n')
                CP_file_name_dict = {}
                CP_file_contents_dict = {}
                for file_count in range(1, number_of_files + 1):
                    CP_file_name = input('    File #' + str(file_count) + ': ')
                    CP_file_name_list.append(CP_file_name)
                    CP_file_name_dict[file_count] = CP_file_name
                    CP_file_contents_dict[file_count] = {}
                print('\nOK! Now assign each pair of characters and their encrypted versions to a file.')
                for char in new_cipher:
                    print('\nFile Name Choices:')
                    for file_number in CP_file_name_dict:
                        print('    (' + str(file_number) + ') ' + CP_file_name_dict[file_number])
                    file_choice = False
                    while not(file_choice):
                        file_choice = input('\n' + char + ' = ' + new_cipher[char] + ' -> Choice #')
                        try:
                            file_choice = int(file_choice)
                            print('OK! That pair will be stored in ' + CP_file_name_dict[file_choice] + '\n')
                            CP_file_contents_dict[file_choice][char] = new_cipher[char]
                        except:
                            print('Invalid input! Please enter an integer that has been assigned to one of your file names.')
                            file_choice = False
                print('\nOK! You have assigned every character to a file name. CustomEncryptor will now create those files.')
                for file_number in range(1, number_of_files + 1):
                    print('Creating ' + CP_file_name_dict[file_number] + '..........')
                    pickle.dump(CP_file_contents_dict[file_number], open(CP_file_name_dict[file_number], 'wb'))
                print('\nOK! Your Cipher Portion files have been created. If they are all in the same folder, be sure to separate them.')                   
        # Automatic - This for loop automatically divides up the new cipher into separate Cipher Portion (CP) files
          # I decided that CP's should contain 5% to 50% of the total cipher. Feel free to change this
            elif gear == 'automatic':
                print('\nOK! Your cipher will be divided into ' + str(number_of_files) + ' files automatically at random.')
                minimum_CP_size_percent = .05
                maximum_CP_size_percent = .50
                minimum_CP_size = int((10 ** len(str(len(new_cipher)))) * minimum_CP_size_percent) + 1
                maximum_CP_size = int(len(new_cipher) * maximum_CP_size_percent) + 1
                character_list = list(new_cipher)
                assigned_already = []
                not_assigned = character_list
                for file_count in range(number_of_files):
                    new_CP = {}
                    if file_count == number_of_files:
                        new_CP_size = len(not_assigned)
                    else:
                        new_CP_size = random.randint(minimum_CP_size, min(maximum_CP_size, (len(not_assigned)) - ((number_of_files - file_count) * minimum_CP_size)))
                        if len(not_assigned) - new_CP_size > maximum_CP_size:
                            new_CP_size += ((len(not_assigned) - new_CP_size) - maximum_CP_size)
                    for char_count in range(new_CP_size):
                        if len(not_assigned) == 1:
                            new_char = new_cipher[not_assigned[0]]
                        else:
                            new_char = random.choice(not_assigned)
                        new_CP[new_char] = new_cipher[new_char]
                        assigned_already.append(new_char)
                        not_assigned.remove(new_char)
                    new_CP_file_name = 'CP_' + str(file_count) + '.pickle'
                    CP_file_name_list.append(new_CP_file_name)
                    pickle.dump(new_CP, open(new_CP_file_name, 'wb'))
                    print('New Cipher Portion file "' + new_CP_file_name + '" with length ' + str(len(new_CP)) + ' has been generated!')
        # This while loop allows the user to choose between saving their CP file locations in their own file
            location_file_creation_input = False
            while not(location_file_creation_input):
                location_file_creation_input = str(input("\nWould you save your Cipher Portion file locations in a file?\n(1) : Save Locations\n(2) : Don't Save\n\nChoice : "))
                if location_file_creation_input.lower() == 'save' or location_file_creation_input == '1':
                    location_file_creation_input = 'save'
                elif location_file_creation_input.lower() == 'no' or location_file_creation_input.lower() == 'no save' or location_file_creation_input == '2':
                    location_file_creation_input = 'no save'
                else:
                    location_file_creation_input = False
                    print('That input was invalid! Please enter "1", "2", "save" or "no save".')
            if location_file_creation_input == 'save':
                print('\nOK! Your Cipher Portion locations will be saved in "NEW CipherLocations.txt"')
                combined_file_names = ''
                for file_name in CP_file_name_list:
                    combined_file_names += file_name
                    combined_file_names += '\n'
                CP_location_file = open('NEW CipherLocations.txt', 'w')
                CP_location_file.write(combined_file_names)
                CP_location_file.close()
            else:
                print('\nOK! Your Cipher Portion locations will not be saved.')
                
        
