def encode(msg, a, b):
    """
    Purpose:- This function is designed to encode the given message.
    Input:-   msg:takes string value as an input.
    Output:-  Returns encoded message.
    """
    ecd = ""

    for i in msg:
        if i.islower():
            ecd += chr(((a * (ord(i) - 97)) + b) % (
                26) + 97)  # converting character to ascii value then performing (P+K) mod 26 to encode the msg.
        elif i.isupper():
            ecd += chr(((a * (ord(i) - 65)) + b) % 26 + 65)
        else:
            ecd += i

    return ecd


def decode(msg, a, b):
    
    # Purpose:- This function is designed to decode the given message.

    if mod_inverse(a, 26) is None:
        return None
    dcd = ""
    for i in msg:
        if i.islower():
            dcd += chr(((mod_inverse(a, 26)) * (
                    ord(i) - 97 - b) % 26) + 97)  # converting character to ascii value then performing (P-K) mod
            # 26 to decode the msg.
        elif i.isupper():
            dcd += chr(((mod_inverse(a, 26)) * (ord(i) - 65 - b) % 26) + 65)
        else:
            dcd += i

    return dcd


def mod_inverse(a, b):
    for i in range(1, b):
        flag = (a * i) % b
        if flag == 1:
            return i
    return None


def main():
    msg = input("Enter the message to encode : ")

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    en = encode(msg, a, b)
    print("The message you entered:", msg)
    print("The message after encryption :", en)
    if decode(en, a, b) is None:
        print("Sorry!! This message can not be decrypted.")
    else:
        print("The message after decryption it :", decode(en, a, b))


if __name__ == '__main__':
    main()
