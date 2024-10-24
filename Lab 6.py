#Andrew George
def encode():
    password = input("Please enter your password to encode: ")
    print("Your password has been encoded and stored!\n")
    new_password = ''
    for i in range(len(password)):
        new_password  += str((int(password[i]) + 3) % 10)
    return new_password
#Minaya Amarasekera
def decode(digits):
    old_password = ''
    for i in range(len(digits)):
        a = (int(digits[i])-3 + 10)%10
        old_password += str(a)
    return old_password

if __name__ == '__main__':

    choice = ''
    while choice != '3':
        print('Menu')
        print('-' * 13)
        print('1.\tEncode')
        print('2.\tDecode')
        print('3.\tQuit\n')
        choice = input("Please enter an option: ")
        if choice == '1':
            encoded_password = encode()
        elif choice == '2':
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
        elif choice == '3':
            break