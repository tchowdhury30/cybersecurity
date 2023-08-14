from a import *

def encode(file, keytext):
    f = open(file, "r")
    f = open(file, "r")
    plain = f.read()
    plain = plain.strip('\n')
    g = open(keytext, "r")
    key= g.read()
    key = key.strip('\n')
    coun = 0
    result = ""
    for i in plain.upper():
        char = key[coun:coun+1].upper()
        #print("char is", char)
        if (coun == len(key)-1 ):
            coun = 0
        else:
            coun+= 1
        shift = 26 - (90 - ord(char) + 1)
        if (ord(i) + shift > 90):
            ans = chr((ord(i) + shift - 90) + 64)
        else:
            ans = chr(ord(i) + shift)
        #print(shift, ord(char), ans)
        result += ans
    return result

def decode(file, keyfile):
    with open(file, "r") as text:
        ciphertext = text.read()
    ciphertext = ciphertext.upper()
    ciphertext = ciphertext.strip("\n")
    with open(keyfile, "r") as text2:
        key = text2.read()
    key = key.upper()
    key = key.strip("\n")

    output = ''
    for i, c in enumerate(ciphertext):
        letter = ord(c)
        new = ord(key[i % len(key)])
        if c.isupper():
            reg = (letter - new) % 26 + 65
            output += chr(reg)
        elif c.islower():
            reg = (letter - new) % 26 + 97
            output += chr(reg)
        else:
            output += c
    return output

def crack(text):
    keys = [""] * 10
    cracked = [""] * 10
    english = frequency(open("alice.txt").read())

    for keyn in range(1,10):
        bucket = [""] * keyn

        for i in range(len(text)): #split into keyn sized strings (1,9)
            bucket[i%keyn] += (text[i])

        for i in range(keyn): #bucket decode
            [a,b] = ciphershift(bucket[i])
            bucket[i] = a
            keys[keyn] += b

        for i in range(len(text)):
            cracked[keyn] += bucket[i%keyn][i//keyn]

    cracked.pop(0)
    keys.pop(0)

    final = distance(english, frequency(cracked[0]))
    ans = cracked[0]
    realKey = keys[0]
    for i in range(len(cracked)):
        dist = distance(english, frequency(cracked[i]))
        if  dist < final:
            ans = cracked[i]
            realKey = keys[i]
            final = dist

    return ans, realKey

def main(func, file1, file2=""):
    if (func == "c"):
        text = open(file1).read()
        print(crack(text)[0])
    if (func == "e"):
        print( encode(file1, file2) )
    if (func == "d"):
        print( decode(file1, file2) )
    if (func == "g"):
        text = open(file1).read()
        print( crack(text)[1] )

if (sys.argv[1] == "e" or sys.argv[1] == "d"):
    main(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    main(sys.argv[1], sys.argv[2])
