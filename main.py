


# Cecelia Beringer
def encode(password):

    new_string = ''


    for i in password:
        new_value = int(i)

        x = new_value + 3

        y = str(x)

        new_string += y


    return new_string






print(encode("12345555"))