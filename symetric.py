from Crypto import Random  # use to generate a random byte string of a length we decide
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import main
# Builtins
import base64
import hashlib
from pyDes import *

'''
https://tutorialsoverflow.com/python-encryption-and-decryption/
'''

"""
# Block sizes for AES encryption is 16 bytes or 128 bits. When AES encryption taking place it will divide our data
# into blocks of length 16. This is a fixed size. So what if your data is smaller than the blocksize ? That’s where
# padding comes into play. Now we need to create a padding function. And also we need to create a unpadding function
# so that we can remove the padding during our encryption process.
"""

BS = 16


# pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
# unpad = lambda s: s[0:-s[-1]]
def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def unpad(s):
    return s[0:-s[-1]]


class AESCipher:

    def __init__(self, key):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()

    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode('utf8')))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:]))


'''
cipher = AESCipher('mysecretpassword')
encrypted = cipher.encrypt('Secret Message A')
decrypted = cipher.decrypt(encrypted)
print(encrypted.decode())
print(decrypted.decode())
'''


# https://stackoverflow.com/questions/42568262/how-to-encrypt-text-with-a-password-in-python/44212550#44212550
# Here's how to do it properly in CBC mode, including PKCS#7 padding:

def encryptAES(key, source, encode=True):
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = Random.new().read(AES.block_size)  # generate IV
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size  # calculate needed padding
    source += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
    data = IV + encryptor.encrypt(source)  # store the IV at the beginning and encryptAES
    return base64.b64encode(data).decode("latin-1") if encode else data


def decryptAES(key, source, decode=True):
    if decode:
        source = base64.b64decode(source.encode("latin-1"))
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = source[:AES.block_size]  # extract the IV from the beginning
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])  # decryptAES
    padding = data[-1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
    if data[-padding:] != bytes([padding]) * padding:  # Python 2.x: chr(padding) * padding
        raise ValueError("Invalid padding...")
    return data[:-padding]  # remove the padding


# Now if you test it as:
def AESenc():
    my_password = input("Please input a secret").encode()
    data = input("Please input a string that you want to encrypt").encode()
    encrypted = encryptAES(my_password, data)
    print("encrypted data: ", encrypted)
    menu_symetric()


def AESdec():
    my_password = input("Please input a secret").encode()
    data = input("Please input a string that you want to decrypt")
    try:
        decrypted = decryptAES(my_password, data)
        print("Congratulations data decrypted succsessfully")
        print("decrypted data: ", decrypted.decode())
        menu_symetric()
    except ValueError:
        print("Secret is not correct")
        menu_symetric()


'''
my_password = b"secret_AES_key_string_to_encrypt/decrypt_with"
my_data = b"input_string_to_encrypt/decryptAES"

print("key:  {}".format(my_password.decode()))
print("data: {}".format(my_data.decode()))
encrypted = encryptAES(my_password, my_data)
print("\nenc:  {}".format(encrypted))
decrypted = decryptAES(my_password, encrypted)
print("dec:  {}".format(decrypted.decode()))
print("\ndata match: {}".format(my_data == decrypted))
print("\nSecond round....")
encrypted = encryptAES(my_password, my_data)
print("\nenc:  {}".format(encrypted))
decrypted = decryptAES(my_password, encrypted)
print("dec:  {}".format(decrypted.decode()))
print("\ndata match: {}".format(my_data == decrypted))
'''


def encryptDES(data, key):
    # data = "Please encrypt my data"
    k = des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(data)
    return d
    # print ("Decrypted: %r" % k.decrypt(d).decode())
    # assert k.decrypt(d, padmode=PAD_PKCS5) == data


def decryptDES(data, key):
    # data = "Please encrypt my data"
    k = des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

    return k.decrypt(data).decode()


def DESenc():
    my_password = input("Please input a secret")
    data = input("Please input a string that you want to encrypt")
    encrypted = encryptDES(data, my_password)
    print("encrypted data: ", encrypted)
    menu_symetric()


def DESdec():
    my_password = input("Please input a secret")
    data = input("Please input a string that you want to decrypt").encode()
    k = des(my_password, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    print(data)
    #decrypted = decryptDES(data, my_password)
    print("Congratulations data decrypted succsessfully")
    print("decrypted data: ", k.decrypt(data).decode())
    menu_symetric()


def menu_symetric():
    print("1: Encrypt AES ")
    print("2: Decrypt AES ")
    print("3: Encrypt DES ")
    print("4: decrypt DES ")
    print("5: Encrypt blowfish ")
    print("6: decrypt blowfish ")
    print("7: Return ")
    while True:
        choix_1_1 = int(input("please type your choice : "))
        try:
            if choix_1_1 in [1, 2, 3, 4, 5, 6, 7]:

                if choix_1_1 == 1:
                    AESenc()
                    break
                if choix_1_1 == 2:
                    AESdec()
                    break
                if choix_1_1 == 3:
                    DESenc()
                    break
                if choix_1_1 == 4:
                    DESdec()
                    break
                elif choix_1_1 == 5:
                    main.menu()
                    break
                elif choix_1_1 == 6:
                    main.menu()
                    break
                elif choix_1_1 == 7:
                    main.menu()
                    break

            else:
                print("Please provide integer between 1 and 5")

        except ValueError:
            print("Please provide integer")
            break
