import main
import base64


def base64_encoding(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def hex_encoding(ascii):
    # Initialize final String
    hexa = ""

    # Make a loop to iterate through
    # every character of ascii string
    for i in range(len(ascii)):
        # take a char from
        # position i of string
        ch = ascii[i]

        # cast char to integer and
        # find its ascii value
        in1 = ord(ch)

        # change this ascii value
        # integer to hexadecimal value
        part = hex(in1).lstrip("0x").rstrip("L")

        # add this hexadecimal value
        # to final string.
        hexa += part

    # return the final string hex
    return hexa


def bin_encoding(message):
    a_byte_array = bytearray(message, "utf8")
    byte_list = []
    for byte in a_byte_array:
        binary_representation = bin(byte)
        byte_list.append(binary_representation)
    return byte_list


def encode_base64():
    msg = input("type a message to be encoded: ")
    # printing original string
    print("The original string is : " + str(msg))
    # printing result
    print("The string after Base 64 encoding : " + base64_encoding(msg))
    encodeing()


def encode_hex():
    msg = input("type a message to be encoded: ")
    # printing original string
    print("The original string is : " + str(msg))
    # printing result
    print("The string after hexadecimal conversion : " + hex_encoding(msg))
    encodeing()


def encode_binary():
    msg = input("type a message to be encoded: ")
    # printing original string
    print("The original string is : " + str(msg))
    # printing result
    print("The string after binary conversion : ")
    print(bin_encoding(msg))
    encodeing()


def encodeing():
    print("1: Base64 ")
    print("2: Hex ")
    print("3: Binary ")
    print("4: Return ")
    while True:
        choix_1_1 = int(input("please type your choice : "))
        try:
            if choix_1_1 in [1, 2, 3, 4]:

                if choix_1_1 == 1:
                    encode_base64()
                    break
                if choix_1_1 == 2:
                    encode_hex()
                    break
                if choix_1_1 == 3:
                    encode_binary()
                    break
                elif choix_1_1 == 4:
                    main.encode_decode()
                    break

            else:
                print("Please provide integer between 1 and 4")

        except ValueError:
            print("Please provide integer")
            break