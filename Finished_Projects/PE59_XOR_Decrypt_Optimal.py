import time

#this uses frequency analysis on the cipher.
#iterate over the cipher in ranges of 3 and get the most common values for each position
def getKey(cipher, sizeKey) :
    freqNumInABC = [{}, {}, {}]
    key = [0 for i in range(sizeKey)]
    for i in range(sizeKey) :
        maxValue = 0
        for j in range(i, len(cipher), 3) :
            if cipher[j] in freqNumInABC[i] :
                freqNumInABC[i][cipher[j]] += 1
            else :
                freqNumInABC[i][cipher[j]] = 1
            if freqNumInABC[i][cipher[j]] > maxValue :
                maxValue = freqNumInABC[i][cipher[j]]
                key[i] = cipher[j]
    for i in range(sizeKey) :
        key[i] = key[i] ^ ord(' ')
    return key

def decryptMsg(cipher, key) :
    plaineTxtASCII = []
    for i in range(0, len(cipher), 3) :
        tmp = cipher[i: i + len(key)]
        plaineTxtASCII += [a ^ b for a, b in zip(tmp, key)]
    return plaineTxtASCII

def main() :
    delta = time.time()
    f = open('\\PATH\\TO\\FILE\\p059_cipher.txt', 'r')
    cipher = f.read().split(',')
    cipher[-1] = cipher[-1][:-1]
    cipher = list(map(int, cipher))
    sizeKey = 3
    key = getKey(cipher, sizeKey)
    decryptedMsgASCII = decryptMsg(cipher, key)
    sumASCII = sum(decryptedMsgASCII)
    decryptedMsg = "".join(chr(a) for a in decryptedMsgASCII)
    delta = time.time() - delta
    return sumASCII, delta

print(main())
