from morse_code_reference import solution_dict


def to_morse_code(str_input):
    encoded_output = ""
    for letter in str_input:
        if letter == ' ':
            encoded_output = encoded_output + '/ '
        else:
            try:
                encoded_output = encoded_output + solution_dict[letter] + ' '
            except KeyError:
                pass
    return encoded_output


def get_key_morse(morse_letter):
    for i in solution_dict:
        if solution_dict[i] == morse_letter:
            return i
    return ""


def to_decode(code_input):
    decoded_output = ""
    words = code_input.split("/")
    for word in words:
        new_letter = ""
        for letter in word:
            if letter == " ":
                decoded_output = decoded_output + get_key_morse(new_letter)
                new_letter = ""
                continue
            new_letter = new_letter + letter

        decoded_output = decoded_output + get_key_morse(new_letter) + " "

    return decoded_output
