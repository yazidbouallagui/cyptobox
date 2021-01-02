import os
import sqlite3 as sql
import hashing
import main

conn = sql.connect('hash_db.db')
c = conn.cursor()


def register_wordlist():
    c.execute(
        "create table if not exists hashs(id integer PRIMARY KEY AUTOINCREMENT,plane text,hash_hex text,"
        "hash_b64 text,type text);")
    fill_file = input("Please past your wordlist in the file wordlist.txt each word in a line then type 'ok'\n")
    if fill_file == "ok":
        filesize = os.path.getsize("wordlist.txt")
        if filesize != 0:
            f = open("wordlist.txt", "r", encoding="utf-8")
            i = 0
            for x in f:
                i = i + 1
                # MD5 crypt and add to hashs bank
                list_word_type = [x.rstrip("\n"), "md5"]
                c.execute("select * from hashs where plane=? and type=?;", list_word_type)
                line = c.fetchone()
                if line is not None:
                    pass
                else:
                    plane = x.rstrip('\n')
                    hash_hex = hashing.md5_encrypt(x.rstrip('\n'), 'hex')
                    hash_b64 = hashing.md5_encrypt(x.rstrip('\n'), 'base64')
                    hash_type = 'md5'
                    list_hashs = [plane, hash_hex, hash_b64, hash_type]
                    c.execute("insert into hashs(plane,hash_hex,hash_b64,type) values(?,?,?,?);", list_hashs)

                # SHA1 crypt and add to hashs bank
                list_word_type = [x.rstrip("\n"), "sha1"]
                c.execute("select * from hashs where plane=? and type=?;", list_word_type)
                line = c.fetchone()
                if line is not None:
                    plane = x.rstrip('\n')
                else:
                    plane = x.rstrip('\n')
                    hash_hex = hashing.sha1_encrypt(x.rstrip('\n'), 'hex')
                    hash_b64 = hashing.sha1_encrypt(x.rstrip('\n'), 'base64')
                    hash_type = 'sha1'
                    list_hashs = [plane, hash_hex, hash_b64, hash_type]
                    c.execute("insert into hashs(plane,hash_hex,hash_b64,type) values(?,?,?,?);", list_hashs)

                # SHA256 crypt and add to hashs bank
                list_word_type = [x.rstrip("\n"), "sha256"]
                c.execute("select * from hashs where plane=? and type=?;", list_word_type)
                line = c.fetchone()
                if line is not None:
                    plane = x.rstrip('\n')
                else:
                    plane = x.rstrip('\n')
                    hash_hex = hashing.sha256_encrypt(x.rstrip('\n'), 'hex')
                    hash_b64 = hashing.sha256_encrypt(x.rstrip('\n'), 'base64')
                    hash_type = 'sha256'
                    list_hashs = [plane, hash_hex, hash_b64, hash_type]
                    c.execute("insert into hashs(plane,hash_hex,hash_b64,type) values(?,?,?,?);", list_hashs)

                # SHA512 crypt and add to hashs bank
                list_word_type = [x.rstrip("\n"), "sha512"]
                c.execute("select * from hashs where plane=? and type=?;", list_word_type)
                line = c.fetchone()
                if line is not None:
                    plane = x.rstrip('\n')
                else:
                    plane = x.rstrip('\n')
                    hash_hex = hashing.sha512_encrypt(x.rstrip('\n'), 'hex')
                    hash_b64 = hashing.sha512_encrypt(x.rstrip('\n'), 'base64')
                    hash_type = 'sha512'
                    list_hashs = [plane, hash_hex, hash_b64, hash_type]
                    c.execute("insert into hashs(plane,hash_hex,hash_b64,type) values(?,?,?,?);", list_hashs)
                conn.commit()

        else:
            print("File empty")
            hash_cracking_menu()
    else:
        hash_cracking_menu()


def register_word(x):
    # MD5 crypt and add to hashs bank
    list_word_type = [x.rstrip("\n"), "md5"]
    c.execute("select * from hashs where plane=? and type=?;", list_word_type)
    line = c.fetchone()
    if line is not None:
        plane = x.rstrip('\n')
    else:
        plane = x.rstrip('\n')
        hash_hex = hashing.md5_encrypt(x.rstrip('\n'), 'hex')
        hash_b64 = hashing.md5_encrypt(x.rstrip('\n'), 'base64')
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
        hash_hex = hashing.sha1_encrypt(x.rstrip('\n'), 'hex')
        hash_b64 = hashing.sha1_encrypt(x.rstrip('\n'), 'base64')
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
        hash_hex = hashing.sha256_encrypt(x.rstrip('\n'), 'hex')
        hash_b64 = hashing.sha256_encrypt(x.rstrip('\n'), 'base64')
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
        hash_hex = hashing.sha512_encrypt(x.rstrip('\n'), 'hex')
        hash_b64 = hashing.sha512_encrypt(x.rstrip('\n'), 'base64')
        hash_type = 'sha512'
        list_hashs = [plane, hash_hex, hash_b64, hash_type]
        c.execute("insert into hashs(plane,hash_hex,hash_b64,type) values(?,?,?,?);", list_hashs)
        conn.commit()



def crack_word():
    hash_to_crack = input("please type the hash in hex or base64 : ")
    list_hash = [hash_to_crack.rstrip("\n"), hash_to_crack.rstrip("\n")]
    c.execute("select * from hashs where hash_hex=? OR hash_b64=?;", list_hash)
    line = c.fetchone()
    if line is None:
        print("Hash can't be cracked now or not real hash register more wordlists then try again")
        hash_cracking_menu()
    else:
        print("Congratulaions Hash cracked successfully !")
        print("Hash : ", hash_to_crack.rstrip("\n"))
        print("Type : ", line[4])
        print("Plane : ", line[1])
        hash_cracking_menu()


def hash_cracking_menu():
    print("1: register a wordlist ")
    print("2: register a word ")
    print("3: crack hash ")
    print("4: Return ")
    while True:
        choix_1_1 = int(input("please type your choice : "))
        try:
            if choix_1_1 in [1, 2, 3, 4]:

                if choix_1_1 == 1:
                    register_wordlist()
                    break
                if choix_1_1 == 2:
                    word = input("please type the word you'd like to regiser : ")
                    register_word(word)
                    print("word registred successfully")
                    hash_cracking_menu()
                    break
                if choix_1_1 == 3:
                    crack_word()
                    break
                elif choix_1_1 == 4:
                    main.menu()
                    break

            else:
                print("Please provide integer between 1 and 4")

        except ValueError:
            print("Please provide integer")
            break
