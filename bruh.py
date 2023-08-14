import numpy as np

# Function to convert string to numbers
def str_to_num(s):
    return [ord(c) - ord('A') for c in s]

# Function to convert numbers to string
def num_to_str(nums):
    return ''.join(chr(n + ord('A')) for n in nums)

# Function to calculate modular inverse
def mod_inverse(n, m=26):
    for i in range(1, m):
        if (n * i) % m == 1:
            return i
    return None

# Function to calculate inverse of matrix
def matrix_inverse(matrix, mod=26):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det, mod)
    if det_inv is None:
        raise ValueError('Matrix is not invertible')
    inv = np.linalg.inv(matrix) * det * det_inv
    return np.round(inv).astype(int) % mod

# Convert key and ciphertext to numbers
key_matrix = np.array(str_to_num('NOOB')).reshape(2, 2)
ciphertext_blocks = np.array(str_to_num('UPGTMQGTVMEGMR')).reshape(-1, 2)

# Calculate inverse of key matrix
key_matrix_inv = matrix_inverse(key_matrix)

# Decrypt the ciphertext
plaintext_blocks = (np.dot(ciphertext_blocks, key_matrix_inv) % 26).astype(int)
plaintext = num_to_str(plaintext_blocks.flatten())

print('Decrypted message:', plaintext)
