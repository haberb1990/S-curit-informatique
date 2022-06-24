def string_to_chars(string):
    """
    Convert a string to a list of chars
    Example: “Alain Tapp” = [A,l,a,i,n,_,T,a,p,p]
    :param string: String to convert to Char
    :return: list of chars
    """
    list_char = []
    for element in string:
        list_char.append(element)
    return list_char


def int_to_8bits(letter):
    """
    Convert letter to an 8 bits binary
    :param letter: letter to convert
    :return: 8 bits binary
    """
    eight_bits = ""
    # convert letter to integer Example: 'A' --> 65
    letter_2_number = ord(letter)
    # Convert integer to binary
    int_2_binary = "{0:b}".format(letter_2_number)
    # Add leading zeros to a number if the length is not 8
    eight_bits = int_2_binary.zfill(8)
    return eight_bits


def list_of_binary(list_char):
    """
    Create a liste of binary from a list of chars
    :param list_char: list to convert to binary
    :return: list of binary numbers (8 bits)
    """
    list_binary = []
    for char in list_char:
        list_binary.append(int_to_8bits(char))
    return list_binary


def concat_list_binary(list_binary):
    """
    Concat a list of binary numbers to a single string
    :param list_binary: list of binary
    :return: one binary string
    """
    binary_string = ""
    for b in list_binary:
        binary_string += b
    return binary_string


def bin_2_int(binary_number):
    """
    Convert binary to intger
    :param binary_number: binary number to convert
    :return: integer
    """
    return int(binary_number, 2)


def cipher(m, n, e):
    """
    Cipher the message with the public key
    :param m: message
    :param n: N -> public key(N,e)
    :param e: e -> public key(N,e)
    :return: C
    """
    return m ** e % n


def main():
    # define N
    file_open = open("N.txt", 'r', encoding='utf-8')
    n = int(file_open.readline())
    file_open.close()

    # Define e
    e = 3

    # C value we are looking for
    c_answer_file = open("C.txt", 'r')
    c_answer = int(c_answer_file.readline())
    c_answer_file.close()

    # Define m
    author_list = []
    file_author = open('listDeAuthF.txt', 'r', encoding='utf-8')
    for line in file_author:
        line_stripped = line.rstrip()
        author_list.append(line_stripped)

    for i in range(0, len(author_list)):
        m = bin_2_int(concat_list_binary(list_of_binary(string_to_chars(author_list[i]))))
        c = cipher(m, n, e)
        if c == c_answer:
            print(author_list[i])
            break

    file_author.close()
main()
