<!--
*** Do a search and replace for the following:
*** EvanGottschalk, CustomEncryptor, Fort1Evan, magnus5557@gmail.com, CustomEncryptor, A simple, customizable program for encrypting and decrypting data
-->



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
    <a href="https://github.com/EvanGottschalk/CustomEncryptor">View Demo</a>
    ·
    <a href="https://github.com/EvanGottschalk/CustomEncryptor/issues">Report Bug</a>
    ·
    <a href="https://github.com/EvanGottschalk/CustomEncryptor/issues">Request Feature</a>
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

### Prerequisites

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

### Installation

1. Download the program files
2. Use the program to create a cipher using `generateCipher()`
3. Divide the cipher into multiple files*
4. Save the portions of the cipher in multiple locations, and record the locations in a file*
5. Congratulations! You can now use `encrypt()` to encrypt data and `decrypt()` to decrypt it later!

\**Steps 3 and 4 require manual file management. These features will be modified to be more automated and user-friendly.*


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/EvanGottschalk/CustomEncryptor/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@Fort1Evan](https://twitter.com/Fort1Evan) - magnus5557@gmail.com

Project Link: [https://github.com/EvanGottschalk/CustomEncryptor](https://github.com/EvanGottschalk/CustomEncryptor)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/EvanGottschalk/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/EvanGottschalk/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/EvanGottschalk/repo.svg?style=for-the-badge
[forks-url]: https://github.com/EvanGottschalk/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/EvanGottschalk/repo.svg?style=for-the-badge
[stars-url]: https://github.com/EvanGottschalk/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/EvanGottschalk/repo.svg?style=for-the-badge
[issues-url]: https://github.com/EvanGottschalk/repo/issues
[license-shield]: https://img.shields.io/github/license/EvanGottschalk/repo.svg?style=for-the-badge
[license-url]: https://github.com/EvanGottschalk/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/EvanGottschalk
