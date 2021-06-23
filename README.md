<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/EvanGottschalk/CustomEncryptor">
    <img src="images/logo.png" alt="Logo" width="151" height="80">
  </a>

  <h3 align="center">CustomEncryptor</h3>

  <p align="center">
    A simple, customizable program for encrypting and decrypting data
    <br />
    <a href="https://github.com/EvanGottschalk/CustomEncryptor"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/EvanGottschalk/CustomEncryptor/issues">Report Bug</a>
    ·
    <a href="https://github.com/EvanGottschalk/CustomEncryptor/issues">Request Feature</a>
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project

### CustomEncryptor.py

`CustomEncryptor` is a cryptography program used to encrypt data by converting it to seemingly random numbers. This is done via a custom cipher: users get to choose the way each character is mapped, thus guaranteeing a unique means of encryption and decryption. Alternatively, `CustomEncryptor` can also be used to generate a cipher on its own using random numbers, which saves users the effort of assigning characters one at a time.

The cipher can then be broken up into multiple files, which increases its efficacy. By using `FetchEncryptedFiles.py`, users can save parts of their cipher in an encrypted zip folder and access them when needed. This is particularly useful when paired with removable storage. By saving a portion of one's cipher in an encrypted zip folder on a flash drive or other removable device, one can essentially use that removable device as a hardware key.

The ultimate goal is to protect users' data by allowing them to avoid saving their sensitive data in files. Instead, users can save encrypted versions of the data, and have the actual data itself nowhere on their device. This means that an adversary would need to obtain all of a user's cipher portions in addition to an encrypted file to be able to read it. If the user utilizes locked zip folders and removable storage, an adversary's job gets even harder. In that case, an adversary would also need the removable storage device, as well as the password to the zip folder.

### FetchEncryptedFiles.py

`FetchEncryptedFiles` is a simple program for retrieving encrypted files on a flash drive or other removable storage. It can be used with `CustomEncryptor` to retrieve important files in an encrypted zip folder that's being stored on removable storage.

### SortDictionary.py

`SortDictionary` is a simple program for sorting dictionaries. It sorts their keys alphabetically, then numerically, and then appends other symbols to the end. It can be used with `CustomEncryptor` to make ciphers more easily read and checked, but it isn't required.



## Prerequisites

The `random` library is used in `CustomEncryptor.py` to encrypt data, and to create new ciphers. It is a default library of Python, so it should only need to be imported.

```sh
import random
```

The `pickle` library is used in `CustomEncryptor.py` and `FetchEncryptedFiles.py` to access and create files. It is a default library of Python, so it should only need to be imported.

```sh
import pickle
```

The `zipfile` library is used in `FetchEncryptedFiles.py` to access encrypted zip folders. If you are not using an encrypted zip folder, particularly one on removable storage, then this library is not necessary. It is a default library of Python, so it should only need to be imported.

```sh
import zipfile
```



## Installation

1. Download the program files
2. Run `generateCipher()` to create your own unique cipher and divide it up into multiple files
3. Congratulations! You can now use `encrypt()` to encrypt data and `decrypt()` to decrypt it later

OPTIONAL: To further increase the efficacy of this program, you can change the function names to obscure their purpose in your other code. For Ctrl+H purposes, here is a list of all the functions and important variables that you may want to use in other programs:

  `CustomEncryptor` - the class name

  `CipherLocations` - the name of the .txt containing your cipher file locations

  `cipher_file` - the variable assigned to the .txt containing your cipher file locations

  `CP_locations_list` - the list of your cipher locations

  `cipher` - the cipher

  `fetchData` - function that attempts to open a file given a location

  `encrypt` - function that encrypts data or a file

  `decrypt` - function that decrypts data or a file

  `generateCipher` - function for creating a brand new cipher

  `byte_length` - the number of digits characters are encrypted to


<!-- USAGE EXAMPLES -->
## Usage

One example of what to use `CustomEncryptor` for is the safe storing of API keys. If you have API keys that you want to access quickly and easily, it is convenient to have them saved somewhere. However, there is an inherent security risk in saving your API keys on your device. Therefore, you can reduce the risk by saving encrypted versions of your API keys instead of the keys themselves.

First, follow the **Installation** instructions to create your own unique cipher.

```sh
CE = CustomEncryptor()
CE.generateCipher()
```

Next, save your API key in a file or copy it to your clipboard. Then, run the `encrypt()` function and either input the name of the file containing your API key, or paste the API key in as a `str`.

```sh
encrypted_key = CE.encrypt(`YOUR_API_KEY_OR_FILE NAME')
```

Finally, save your encrypted key in a new file.

That's it! You may now use the `decrypt()` function in your other code to access your API key, without ever having the API key saved on your device.

## Functions

`assembleCipher()` - puts your complete cipher together from the various Cipher Portion files

`generateCipher()` - creates a new cipher and group of Cipher Portion files to user's specifications

`encrypt(file_info)` - uses the most recently assembled cipher to encrypt the file `file_info` refers to. If it can't find a file located at `file_info`, it encrypts the input `str` itself.

More about `encrypt`:

Maximum length - by default, `encrypt` can only encrypt data of 100 characters or less. Change this by altering the value of `encryption_length` in the `__init__`. Keep in mind that, the larger the number you use, the bigger the encrypted outputs will be.
    
Consistent length - the output from `encrypt` will always be the same length. The length is `encryption_length * byte_length`. When encrypting data with fewer than `encryption_length` characters, random characters are added to the end until its length is equal to `encryption_length * byte_length`. Adding extra characters at random is not a problem, because the individual with the right to access the decrypted data will know how long the decrypted version is supposed to be, and can ignore characters beyond that length.

`decrypt(file_info)` - uses the most recently assembled cipher to decrypt the file `file_info` refers to. If it can't find a file located at `file_info`, it attempts to decrypt the input `str` itself.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/EvanGottschalk/CustomEncryptor/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

All feedback is extremely welcome! Getting this program to be as secure and simple as possible is my goal. Please let me know if you see any improvements I can make, or any holes or backdoors that need to be sealed.

Honestly, I was hesitant about publicizing a program I intend to use for my own security purposes. However, I trust that any feedback I get will strengthen `CustomEncryptor` by a much greater amount than sharing the code compromises it.



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Evan Gottschalk - [Evan on LinkedIn](https://www.linkedin.com/in/evan-gottschalk/) - [@Fort1Evan](https://twitter.com/Fort1Evan) - magnus5557@gmail.com

Project Link: [https://github.com/EvanGottschalk/CustomEncryptor](https://github.com/EvanGottschalk/CustomEncryptor)



<!-- ACKNOWLEDGEMENTS -->
<!-- To be filled out later - I may use some code that a friend of mine provided
## Acknowledgements

* []()
* []()
* []()
-->




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/EvanGottschalk/CustomEncryptor.svg?style=for-the-badge
[contributors-url]: https://github.com/EvanGottschalk/CustomEncryptor/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/EvanGottschalk/CustomEncryptor.svg?style=for-the-badge
[forks-url]: https://github.com/EvanGottschalk/CustomEncryptor/network/members
[stars-shield]: https://img.shields.io/github/stars/EvanGottschalk/CustomEncryptor.svg?style=for-the-badge
[stars-url]: https://github.com/EvanGottschalk/CustomEncryptor/stargazers
[issues-shield]: https://img.shields.io/github/issues/EvanGottschalk/CustomEncryptor.svg?style=for-the-badge
[issues-url]: https://github.com/EvanGottschalk/CustomEncryptor/issues
[license-shield]: https://img.shields.io/github/license/EvanGottschalk/CustomEncryptor.svg?style=for-the-badge
[license-url]: https://github.com/EvanGottschalk/CustomEncryptor/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/EvanGottschalk
