import sys

def frequency(text):
    freq = 26 * [0]
    num = 0
    for char in text.lower():
        if char.isalpha():
            freq[ord(char) - 97] += 1
            num+=1
    for i in range(26):
        freq[i] /= num
    return freq

def distance(a, b):
    distance = 0
    for i in range(26):
        distance += pow((a[i] - b[i]), 2)
    distance = pow(distance, 0.5)
    return distance

def ciphershift(text):
    english = frequency(open("alice.txt").read())
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    code = {}
    bfreq = english.copy()
    freq = frequency(text)
    freqCOPY = freq.copy()

    shift = 0
    leastDistance = distance(bfreq,freq)

    for i in range(26):
        for j  in range(26):
            freq[(i + j) % 26] = freqCOPY[j]
        currentDistance = distance(freq, bfreq)
        if currentDistance < leastDistance:
            shift = 26 - i

            for j in range(26):
                code[alphabet[j]] = alphabet[(i+j)%26]
            leastDistance = currentDistance

    uncodedtext = ""
    for char in text:
        if (char.isalpha()):
            if char.isupper():
                uncodedtext += code[char.lower()].upper()
            else:
                uncodedtext += code[char]
        else:
            uncodedtext += char
    lettershift = chr(ord('a') + shift)

    return uncodedtext, lettershift
