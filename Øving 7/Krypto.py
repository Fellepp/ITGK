import binascii
from random import shuffle


def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)


def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')

#a)
def encrypt(message, key):
    messageBinary = bytes(message, encoding = 'ascii')
    keyBinary = bytes(key, encoding = 'ascii')
    messageHex = toHex(messageBinary)
    keyHex = toHex(keyBinary)
    code = messageHex ^ keyHex
    return code

#b)
def decrypt(code, key):
    keyBinary = bytes(key, encoding = 'ascii')
    keyHex = toHex(keyBinary)
    message = code ^ keyHex
    messageString = toString(message)
    return messageString

#c)
def main():
    word = input("Skriv inn en setning: ")
    keyList = list(word)
    shuffle(keyList)
    key = ''.join(keyList)
    code = encrypt(word, key)
    print(code)
    print(decrypt(code, key))

main()






