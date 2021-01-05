import base64
import main
import rsa
from Crypto.PublicKey import RSA
from pathlib import Path


def generate_keys():
    (pubkey, privkey) = rsa.newkeys(2048)
    # print(pubkey)
    # write the public key to a file #
    publickey = open('pubkey.key', 'wb')
    publickey.write(pubkey.save_pkcs1('PEM'))
    publickey.close()
    prkey = open('privkey.key', 'wb')
    prkey.write(privkey.save_pkcs1('PEM'))
    prkey.close()
    response = ""
    while True:
        response = input("would you like to protect the privatekey with passphrase? yes/no")
        if response == "yes" or response == "no":
            break
    if response == "no":
        return pubkey, privkey
    elif response == "yes":
        pass


# print(generate_keys()[0])

def protect_rsa_key(password):
    pem_key = key.export_key(passphrase=password)


def sign_rsa():
    with open('privkey.key', mode='rb') as file:
        keydata = file.read()
    privkey = rsa.PrivateKey.load_pkcs1(keydata)
    message = input("Message to signe").encode()
    signature = rsa.sign(message, privkey, 'SHA-1')
    print("signed message :")
    print(base64.b64encode(signature).decode("latin-1") if base64.encode else signature)
    menu_asymetric()


def verify_rsa():
    message = input("input the message to verify: ").encode()
    signature = input("input the signature")
    signature=base64.b64decode(signature.encode("latin-1"))
    with open('pubkey.key', mode='rb') as file:
        keydata = file.read()
    pubkey = rsa.PublicKey.load_pkcs1(keydata)
    result = rsa.verify(message, signature, pubkey)
    if result:
        print("Signature verified successfully")
    else:
        print("Signature not verified")
    menu_asymetric()


def rsa_encrypt():
    message = input("input the message to encrypt: ").encode()
    with open('pubkey.key', mode='rb') as file:
        keydata = file.read()
    pubkey = rsa.PublicKey.load_pkcs1(keydata)
    crypto = rsa.encrypt(message, pubkey)
    print("encrypted message: ")
    print(base64.b64encode(crypto).decode("latin-1") if base64.encode else crypto)
    menu_asymetric()


def rsa_decrypt():
    message = input("input the message to decrypt: ")
    message = base64.b64decode(message.encode("latin-1"))
    with open('privkey.key', mode='rb') as file:
        keydata = file.read()
    privkey = rsa.PrivateKey.load_pkcs1(keydata)
    crypto = rsa.decrypt(message, privkey).decode()
    print("decrypted message : ")
    print(crypto)
    menu_asymetric()


def menu_asymetric():
    print("1: Generate RSA keypaire ")
    print("2: Encrypt RSA ")
    print("3: Decrypt RSA ")
    print("4: Sign RSA ")
    print("5: Verify RSA")
    print("6: Return ")
    while True:
        choix_1_1 = int(input("please type your choice : "))
        try:
            if choix_1_1 in [1, 2, 3, 4, 5, 6]:

                if choix_1_1 == 1:
                    generate_keys()
                    break
                if choix_1_1 == 2:
                    rsa_encrypt()
                    break
                if choix_1_1 == 3:
                    rsa_decrypt()
                    break
                if choix_1_1 == 4:
                    sign_rsa()
                    break
                elif choix_1_1 == 5:
                    verify_rsa()
                    break
                elif choix_1_1 == 6:
                    main.menu()
                    break


            else:
                print("Please provide integer between 1 and 5")

        except ValueError:
            print("Please provide integer")
            break
