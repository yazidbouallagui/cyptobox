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
    # initializing a empty string for
    # storing the string data
    str_data = ' '

    # slicing the input and converting it
    # in decimal and then converting it in string
    for i in range(0, len(bin_data), 7):
        # slicing the bin_data from index range [0, 6]
        # and storing it as integer in temp_data
        temp_data = int(bin_data[i:i + 7])

        # passing temp_data in BinarytoDecimal() function
        # to get decimal value of corresponding temp_data
        decimal_data = BinaryToDecimal(temp_data)

        # Deccoding the decimal value returned by
        # BinarytoDecimal() function, using chr()
        # function which return the string corresponding
        # character for given ASCII value, and store it
        # in str_data
        str_data = str_data + chr(decimal_data)
        return str_data


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
    print("3: Binary ")
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
                    decode_binary()
                    break
                elif choix_1_1 == 4:
                    main.encode_decode()
                    break

            else:
                print("Please provide integer between 1 and 4")

        except ValueError:
            print("Please provide integer")
            break
