import encode
import decode
import hashing
import hashcracker
import symetric

def encode_decode():
    print("1: Message encoding ")
    print("2: Message Decoding ")
    print("3: Return ")
    while True:
        choix_1 = int(input("please type your choice : "))
        try:
            if choix_1 in [1, 2, 3]:

                if choix_1 == 1:
                    encode.encodeing()
                    break
                if choix_1 == 2:
                    decode.decoding()
                    break
                elif choix_1 == 3:
                    menu()
                    break

            else:
                print("Please provide integer between 1 and 3")

        except ValueError:
            print("Please provide integer")
            break


def menu():
    print(
        "................................................................................\n"
        "................................................................................\n"
        "................................................................................\n"
        ".....................................*%%#%%%....................................\n"
        "...................................#%#......%%#.................................\n"
        "..................................("
        "%#........#%.................................\n..................................###........#%,"
        "................................\n"
        "..................................###........#%.................................\n"
        "...............................##%#%%%#%%%#%%%%%#%*.............................\n"
        "...............................##%%#%%%%%%%%%%%#%%#......,#.....................\n....................*("
        "#..*.,/#/#/#%##%%#..%###%%###...../.......................\n....................#((#,#,.,%*,,"
        "%%%%##....##%%%%%#.......*%%(#.................\n..........................%%.*(.(.,#/%##..#%#%#####.....("
        "//%....................\n..............................*###%%%%#%%%#%%*.##%#.............................\n"
        "...............................####%%%%%%%%%%%###%#.............................\n"
        "................................#################("
        "..............................\n"
        "................................................................................\n"
        "................................................................................")
    print("1: Message encoding /decoding ")
    print("2: Hashing ")
    print("3: Cracking Hashs ")
    print("4: Symetric encryption / decryption ")
    print("5: Asymetric encryption / decryption ")
    print("6: Quit ")
    while True:
        choix = int(input("Donner votre choix : "))
        try:
            if choix in [1, 2, 3, 4, 5]:

                if choix == 1:
                    encode_decode()
                    break
                elif choix == 2:
                    hashing.hashing()
                    break
                elif choix == 3:
                    hashcracker.hash_cracking_menu()
                    break
                elif choix == 4:
                    symetric.menu_symetric()
                    break
                elif choix == 5:
                    asymetric()
                    break
            elif choix == 6:
                print("Goodbye ")
                pass
                break
            else:
                print("Please provide integer between 1 and 6")

        except ValueError:
            print("Please provide integer")
            break

# menu()
