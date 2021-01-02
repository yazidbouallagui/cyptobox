import hashlib
import base64
import main
import sqlite3 as sql

conn = sql.connect('hash_db.db')
c = conn.cursor()


def register_word(x):
    # MD5 crypt and add to hashs bank
    list_word_type = [x.rstrip("\n"), "md5"]
    c.execute("select * from hashs where plane=? and type=?;", list_word_type)
    line = c.fetchone()
    if line is not None:
        plane = x.rstrip('\n')
    else:
        plane = x.rstrip('\n')
        hash_hex = md5_encrypt(x.rstrip('\n'), 'hex')
        hash_b64 = md5_encrypt(x.rstrip('\n'), 'base64')
        hash_type = 'md5'
        list_hashs = [plane, hash_hex, hash_b64, hash_type]
        c.execute("insert into hashs(plane,hash_hex,hash_b64,type) values(?,?,?,?);", list_hashs)
        conn.commit()
    # SHA1 crypt and add to hashs bank
    list_word_type = [x.rstrip("\n"), "sha1"]
    c.execute("select * from hashs where plane=? and type=?;", list_word_type)
    line = c.fetchone()
    if line is not None:
        plane = x.rstrip('\n')
    else:
        plane = x.rstrip('\n')
        plane = x.rstrip('\n')
        hash_hex = sha1_encrypt(x.rstrip('\n'), 'hex')
        hash_b64 = sha1_encrypt(x.rstrip('\n'), 'base64')
        hash_type = 'sha1'
        list_hashs = [plane, hash_hex, hash_b64, hash_type]
        c.execute("insert into hashs(plane,hash_hex,hash_b64,type) values(?,?,?,?);", list_hashs)
        conn.commit()

    # SHA256 crypt and add to hashs bank
    list_word_type = [x.rstrip("\n"), "sha256"]
    c.execute("select * from hashs where plane=? and type=?;", list_word_type)
    line = c.fetchone()
    if line is not None:
        plane = x.rstrip('\n')
    else:
        plane = x.rstrip('\n')
        hash_hex = sha256_encrypt(x.rstrip('\n'), 'hex')
        hash_b64 = sha256_encrypt(x.rstrip('\n'), 'base64')
        hash_type = 'sha256'
        list_hashs = [plane, hash_hex, hash_b64, hash_type]
        c.execute("insert into hashs(plane,hash_hex,hash_b64,type) values(?,?,?,?);", list_hashs)
        conn.commit()

    # SHA512 crypt and add to hashs bank
    list_word_type = [x.rstrip("\n"), "sha512"]
    c.execute("select * from hashs where plane=? and type=?;", list_word_type)
    line = c.fetchone()
    if line is not None:
        plane = x.rstrip('\n')
    else:
        plane = x.rstrip('\n')
        hash_hex = sha512_encrypt(x.rstrip('\n'), 'hex')
        hash_b64 = sha512_encrypt(x.rstrip('\n'), 'base64')
        hash_type = 'sha512'
        list_hashs = [plane, hash_hex, hash_b64, hash_type]
        c.execute("insert into hashs(plane,hash_hex,hash_b64,type) values(?,?,?,?);", list_hashs)
        conn.commit()


def hash_analyser():
    return 1


def md5_encrypt(message, type):
    if type == 'hex':
        result = hashlib.md5(message.encode()).hexdigest()

        return result
    elif type == 'base64':
        result = hashlib.md5(message.encode()).hexdigest()
        result = base64.b64encode(bytes.fromhex(result))
        final = str(result)[2:len(result) + 2:1]

        return final


def sha256_encrypt(message, type):
    if type == 'hex':
        result = hashlib.sha256(message.encode()).hexdigest()
        return result
    elif type == 'base64':
        result = hashlib.sha256(message.encode()).hexdigest()
        result = base64.b64encode(bytes.fromhex(result))[2:]
        final = str(result)[2:len(result) + 2:1]

        return final


def sha512_encrypt(message, type):
    if type == 'hex':
        result = hashlib.sha512(message.encode()).hexdigest()
        return result
    elif type == 'base64':
        result = hashlib.sha512(message.encode()).hexdigest()
        result = base64.b64encode(bytes.fromhex(result))
        final = str(result)[2:len(result) + 2:1]

        return final


def sha1_encrypt(message, type):
    if type == 'hex':
        result = hashlib.sha1(message.encode()).hexdigest()
        return result
    elif type == 'base64':
        result = hashlib.sha1(message.encode()).hexdigest()
        result = base64.b64encode(bytes.fromhex(result))
        final = str(result)[2:len(result) + 2:1]

        return final


def md5_enc():
    msg = input("type a message to be encryped: ")
    # printing original string
    print("The original string is : " + str(msg))
    # printing result
    print("The string after hashing : ")
    print("hex: ")
    print(md5_encrypt(msg, 'hex'))
    print("base64: ")
    print(md5_encrypt(msg, 'base64'))
    register_word(msg)
    hashing()


def sha1_enc():
    msg = input("type a message to be encryped: ")
    # printing original string
    print("The original string is : " + str(msg))
    # printing result
    print("The string after hashing : ")
    print("hex: ")
    print(sha1_encrypt(msg, 'hex'))
    print("base64: ")
    print(sha1_encrypt(msg, 'base64'))
    register_word(msg)
    hashing()


def sha256_enc():
    msg = input("type a message to be encryped: ")
    # printing original string
    print("The original string is : " + str(msg))
    # printing result
    print("The string after hashing : ")
    print("hex: ")
    print(sha256_encrypt(msg, 'hex'))
    print("base64: ")
    print(sha256_encrypt(msg, 'base64'))
    register_word(msg)
    hashing()


def sha512_enc():
    msg = input("type a message to be encryped: ")
    # printing original string
    print("The original string is : " + str(msg))
    # printing result
    print("The string after hashing : ")
    print("hex: ")
    print(sha512_encrypt(msg, 'hex'))
    print("base64: ")
    print(sha512_encrypt(msg, 'base64'))
    register_word(msg)
    hashing()


def hashing():
    print("1: md5 ")
    print("2: sh1 ")
    print("3: sh256 ")
    print("4: sh512 ")
    print("5: Return ")
    while True:
        choix_1_1 = int(input("please type your choice : "))
        try:
            if choix_1_1 in [1, 2, 3, 4, 5]:

                if choix_1_1 == 1:
                    md5_enc()
                    break
                if choix_1_1 == 2:
                    sha1_enc()
                    break
                if choix_1_1 == 3:
                    sha256_enc()
                    break
                if choix_1_1 == 4:
                    sha512_enc()
                    break
                elif choix_1_1 == 5:
                    main.menu()
                    break

            else:
                print("Please provide integer between 1 and 5")

        except ValueError:
            print("Please provide integer")
            break
