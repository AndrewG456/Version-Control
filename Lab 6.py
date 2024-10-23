#Andrew George
def encode():
    password = input("Please enter your password to encode: ")
    print("Your password has been encoded and stored!\n")
    new_password = ''
    for i in range(len(password)):
        new_password  += str((int(password[i]) + 3) % 10)
    return new_password

def decode():
    pass

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
            encode()
        elif choice == '2':
            decode()
        elif choice == '3':
            break