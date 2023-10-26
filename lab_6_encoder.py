# calls the menu
def menu():
    print('Menu')
    print('-' * 13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')



# option 1 which creates the encoder
def encoder(password):
    encoded_list = []
    for num in password:
        new_num = int(num) + 3
        encoded_list.append(new_num)
    return encoded_list


# option 2 which creates the decoder
def decoder(password):
    pass


# program while loop to continue it going
user_continue = True
while user_continue:
    menu()
    user_input = input('Please enter an option')
    if user_input == '1':      # activates the encoder
        user_password = input('Please enter your password to encode: ')
        encoded_list = encoder(user_password)
        for num in encoded_list:
            print(num, end='')
        print()
        print('Have fun with your encoded password!')


    elif user_input == '2':    # activates the decoder
        pass

    elif user_input == '0':    # ends the program
        user_continue = False
