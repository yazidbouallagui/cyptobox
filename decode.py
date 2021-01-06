import base64
import main


def base64_decode(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    return message


def hex_decode(message):
    bytes_object = bytes.fromhex(message)
    ascii_string = bytes_object.decode("ASCII")
    return ascii_string


def BinaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def bin_decode(bin_data):
    binary_int = int(bin_data, 2)
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()

    return ascii_text


def decode_base64():
    msg = input("type a message to be decoded: ")
    # printing original string
    print("The original string is : " + str(msg))
    # printing result
    print("The string after Base 64 encoding : " + base64_decode(msg))
    decoding()


def decode_hex():
    msg = input("type a message to be decoded: ")
    # printing original string
    print("The original string is : " + str(msg))
    # printing result
    print("The string after hexadecimal decoding : " + str(hex_decode(msg)))
    decoding()


def decode_binary():
    msg = input("type a binary sequance  to be decoded: ")
    # printing original string
    print("The original string is : " + str(msg))
    # printing result
    print("The string after binary conversion : " + bin_decode(msg))
    decoding()


def decoding():
    print("1: Base64 ")
    print("2: Hex ")
    #("3: Binary ")
    print("4: Return ")
    while True:
        choix_1_1 = int(input("please type your choice : "))
        try:
            if choix_1_1 in [1, 2, 3, 4]:

                if choix_1_1 == 1:
                    decode_base64()
                    break
                if choix_1_1 == 2:
                    decode_hex()
                    break
                if choix_1_1 == 3:
                    #decode_binary()
                    decoding()
                    break
                elif choix_1_1 == 4:
                    main.encode_decode()
                    break

            else:
                print("Please provide integer between 1 and 4")

        except ValueError:
            print("Please provide integer")
            break
