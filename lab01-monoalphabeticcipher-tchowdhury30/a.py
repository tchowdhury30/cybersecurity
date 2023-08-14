import sys

def frequency(filename):
# 1.1 OPEN SOURCE FILE + ANALYZE LETTER FREQ
    letters_freq = {"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0,
    "h" : 0, "i" : 0, "j" : 0, "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0,
    "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0,
    "z" : 0, }

    with open(filename,"rt") as text:
        contents = text.read()
        contents = contents.lower()

    pos = 0
    total = 0
    while len(contents) > pos:
        if ord(contents[pos]) >= 97 and ord(contents[pos]) <= 122:
            total = total + 1
            letters_freq[contents[pos]] = letters_freq[contents[pos]] + 1
        pos = pos + 1;

    for i in range(26):
        letters_freq[chr(i+97)] = letters_freq[chr(i+97)] / total
        #print( (chr(i+97)).upper(), letters_freq[chr(i+97)])

    return letters_freq

def distance(a, b):
# 1.2 DISTANCE btwn 2 FILE LETTER FREQs SETS
    freq_a = frequency(a)
    freq_b = frequency(b)
    ans = 0
    for i in range(26):
        ans = ans + (freq_a[chr(i+97)] - freq_b[chr(i+97)])**2
        #print(chr(i+97), (freq_a[chr(i+97)] - freq_b[chr(i+97)])**2)
    ans = ans**0.5
    #print("DISTANCE:", ans)
    return ans

def decode(a):
# 1.3 DECODE MSG IN FILE
    ciphered = frequency(a)
    ciphered2 = frequency(a)
    english = frequency("alice.txt")
    dist = distance(a, "alice.txt")
    dist2 = distance(a, "alice.txt")
    shifted = []
    reverse = []
    final = 0
    final2 = 0
    setting = 0

    for i in range(26):
        shifted.append(ciphered[chr(i+97)])

    for i in range(25, -1, -1):
        reverse.append(ciphered[chr(i+97)])

    for i in range(26):
        shifted = shifted[-1:] + shifted[:-1]
        reverse = reverse[-1:] + reverse[:-1]

        for j in range(26): #list->dict
            ciphered[chr(j+97)] = shifted[j]
        for j in range(26):
            ciphered2[chr(j+97)] = reverse[j]

        ans = 0
        for k in range(26): #distance
            ans = ans + (english[chr(k+97)] - ciphered[chr(k+97)])**2
        ans = ans**0.5

        rev = 0
        for k in range(26): #distance REVERSE
            rev = rev + (english[chr(k+97)] - ciphered2[chr(k+97)])**2
        rev = rev**0.5

        if (ans < dist):
            dist = ans
            final = i+1

        if (rev < dist2):
            dist2 = rev
            final2 = 25-i

    if (min(dist, dist2) == dist2):
        final = final2
        setting = -1 #REVERSE

    #print(final, setting)

    with open(a,"rt") as text:
        contents = text.read()

    result = ""
    for i in range(len(contents)):
        char = contents[i]
        if (char.isupper()):
            result += chr((ord(char) + final-65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + final- 97) % 26 + 97)
        else:
            result += char
    #print(result)
    return result

def main(func, file1, file2=""):
    if (func == "freq"):
        myfreq = frequency(file1)
        for i in range(26):
            print( (chr(i+97)).upper(), myfreq[chr(i+97)])
    if (func == "dist"):
        print( distance(file1, file2) )
    if (func == "decode"):
        print( decode(file1) )

if (sys.argv[1] == "dist"):
    main(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    main(sys.argv[1], sys.argv[2])
