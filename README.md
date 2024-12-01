# Cybersecurity Projects Overview

This repository contains various cybersecurity-related projects, including encryption algorithms, cryptography, and image steganography. The main focus of these labs is on implementing classical encryption techniques using Python and C, as well as exploring modern concepts like image data hiding and signal analysis.

## Project Structure

```plaintext
.
├── README.md
├── bruh.py
├── cyberFP
├── lab01-monoalphabeticcipher-tchowdhury30
├── lab02-vigenere-tchowdhury30
├── lab03-xor-tchowdhury30
└── lab05-imagestego-tchowdhury30
```

## 1. `cyberFP` Directory

**Description**:  
This folder contains files for a cybersecurity project focused on **frequency analysis** of **ciphered audio data** and its **visualization**.

- **Key Techniques**:  
    - **Frequency Analysis**: The project involves analyzing the frequency of encrypted audio samples to detect weaknesses in the cipher.
    - **Visualization**: The data is processed using the **Fast Fourier Transform (FFT)** and visualized for better insight.

- **Files**:  
    - **`visualizer.py`**: A Python program that visualizes frequency data from audio files.
    - **`src/`**: Contains various sample audio files used for frequency analysis.

- **Algorithms**:  
    - **Fast Fourier Transform (FFT)**: A signal processing algorithm that converts time-domain data into frequency-domain data for analysis.
    - **Signal Processing**: The project applies signal processing techniques to resample and filter audio data for better frequency visualization.

## 2. `lab01-monoalphabeticcipher-tchowdhury30`

**Description**:  
This project implements a **monoalphabetic substitution cipher**, which is one of the simplest encryption methods.

- **Key Techniques**:  
    - **Monoalphabetic Substitution**: Each letter of the plaintext is substituted with a corresponding letter from a fixed alphabet. A key is used to define the mapping.
    - **Brute Force Decryption**: This method uses a brute-force approach to test all possible cipher keys and decrypt the ciphertext.

- **Algorithms**:  
    - **Substitution Cipher**: A straightforward cipher based on letter substitution.
    - **Frequency Analysis**: An analysis of the letter frequency is used to break the cipher.

- **Files**:  
    - **`a.py`**: Implements the encryption and decryption logic.
    - **`alice.txt`**: Example plaintext used for the cipher.
    - **`test.txt`**: Encrypted message used for testing the decryption.

## 3. `lab02-vigenere-tchowdhury30`

**Description**:  
This project implements the **Vigenère cipher**, a more complex form of encryption that uses a keyword for polyalphabetic substitution.

- **Key Techniques**:  
    - **Vigenère Cipher**: Unlike monoalphabetic substitution, the Vigenère cipher shifts letters by varying amounts based on the keyword. This makes it more secure than simpler ciphers.
    - **Encryption and Decryption**: The Vigenère cipher relies on modular arithmetic for encryption and decryption.

- **Algorithms**:  
    - **Polyalphabetic Substitution**: Each letter in the plaintext is shifted based on the corresponding letter of the key.
    - **Key Cycling**: The key is repeated to match the length of the plaintext, making this cipher more complex and secure than monoalphabetic substitution.

- **Files**:  
    - **`a.py`**: Contains the logic for encryption and decryption.
    - **`cipher.txt`**: Example ciphertext encrypted using the Vigenère cipher.
    - **`plain.txt`**: Plaintext before encryption.

## 4. `lab03-xor-tchowdhury30`

**Description**:  
This project demonstrates the use of **XOR encryption**, a simple yet powerful encryption method based on the XOR bitwise operation.

- **Key Techniques**:  
    - **XOR Operation**: XOR is used as a basic encryption algorithm. The same key is used for both encryption and decryption, making it a symmetric encryption technique.
    - **File Encryption**: The project encrypts and decrypts files using XOR, showing how the technique works on both text and binary files.

- **Algorithms**:  
    - **XOR Encryption**: The XOR bitwise operation is applied between the plaintext and the key.
    - **Bitwise Operations**: This encryption method uses bit-level manipulation for simplicity and efficiency.

- **Files**:  
    - **`lab03.c`**: Implements XOR encryption and decryption in C.
    - **`key`** and **`cipher`**: Example files for testing the XOR encryption.
    - **`makefile`**: Builds and runs the XOR encryption program.

## 5. `lab05-imagestego-tchowdhury30`

**Description**:  
This lab demonstrates **image steganography**, the practice of hiding data in an image without perceptibly altering its appearance.

- **Key Techniques**:  
    - **Image Encoding and Decoding**: Text data is hidden in the least significant bits (LSB) of an image's pixels. This method allows the data to be encoded and decoded without significantly altering the image.
    - **Data Hiding in Images**: This project showcases how images can be used as carriers for hidden data, with a focus on maintaining the integrity of the image.

- **Algorithms**:  
    - **Least Significant Bit (LSB) Encoding**: The least significant bits of the image pixels are modified to hide the secret message.
    - **Image Processing**: Each pixel of the image is processed to encode and decode the hidden data.

- **Files**:  
    - **`image_encoder.pde`**: The code that encodes data into an image using LSB.
    - **`image_decoder.pde`**: The code that decodes the hidden data from an image.
    - **`image_diff.pde`**: Compares the original and modified images to analyze the changes.
    - **`modifiedCat.png`**, **`newmodifiedCat.png`**: Sample images used in the encoding process.

## Conclusion

This repository demonstrates a variety of classic cryptographic techniques and cybersecurity concepts:
- **Encryption Algorithms**: The repository includes implementations of classical ciphers like the **monoalphabetic cipher**, **Vigenère cipher**, and **XOR encryption**, showing foundational cryptographic knowledge.
- **Image Steganography**: The **image steganography** project demonstrates data hiding techniques, an essential area of cybersecurity.
- **DSA**: While data structures and algorithms (DSA) aren't the primary focus, concepts like **XOR** (symmetric encryption) and **message parsing** are relevant and fundamental to these cryptographic implementations.
  
The projects in this repository offer hands-on experience with encryption algorithms, cryptography, and data privacy techniques. They are essential for building a strong foundation in cybersecurity.
