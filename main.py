



# Cecelia Beringer
def encode(password):

    new_string = ''


    for i in password:

        new_value = int(i)


        if new_value > 6:

            new_value = int(i)

            x = (new_value +3) - 10



            y = str(x)

            new_string += y

        else:



            x = new_value + 3

            y = str(x)

            new_string += y






    return new_string


def decode(password):
    final = ''
    for char in password:
        decoded_char = int(char) - 3
        final += str(decoded_char)
    return final



if __name__ == '__main__':

    program = True

while program == True:

    print('Menu')
    print('-------------')
    print('1.Encode')
    print('2.Decode')
    print('3.Quit')

    select = int(input('Please enter an option: '))




    if select == 1:
        password = input('Please enter your password to encode: ')
        encoded_password = encode(password)
        print('Your password has been encoded and stored!')


    if select == 2:
        print('The encoded password is', encoded_password,', and the original password is', decode(encoded_password))


    if select == 3:
        program = False
