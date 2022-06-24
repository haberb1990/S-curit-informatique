"""
The key is exactly the same as the length of message which is encrypted
the length of the key is equal to 9334 which is half of the message
the message is divided in 2 parts: M1 and M2
we apply the xor method between M1 and M2
Reference: http://www.crypto-it.net/eng/attacks/two-time-pad.html
"""


def convert_binary_to_list_of_8bits(str_bin):
    """
    Binary number to split in 8 bits binary
    1111111100000000 => ['11111111','00000000']
    :param str_bin: binary number to split
    :return: list of 8 bits binary number
    """
    list_bin = []
    for bits in range(8, len(str_bin) + 8, 8):
        list_bin.append(str_bin[bits - 8:bits])
    return list_bin


def convert_binarylist_to_integer(list_bin):
    """
    Function that takes in input a list of binary numbers (8 bits each)
    and returns a list of chars that represents the binary list
    Example :
    ['01000001', '01101100', '01100001', '01101001', '01101110',
                        '00100000', '01010100', '01100001', '01110000', '01110000']
    ==  [65, 108, 97, 105, 110, 32, 84, 97, 112, 112]
    :param list_bin: list of binary numbers
    :return: list of integer
    """
    list_int = []
    for bin_number in list_bin:
        number = int(bin_number, 2)
        list_int.append(number)
    return list_int


def convert_integer_to_char(list_int):
    """
    convert list of numbers to list of chars
    [65, 108, 97, 105, 110, 32, 84, 97, 112, 112] ==
    ['A', 'l', 'a', 'i', 'n', ' ', 'T', 'a', 'p', 'p']
    :param list_int: list of numbers
    :return: list of chars
    """
    list_char = []
    for i in list_int:
        list_char.append(chr(i))
    return list_char


def concat_strings(list_char):
    """
    concat the chars into a string
    :param list_char: list of chars
    :return: string
    """
    str_from_chars = ""
    for b in list_char:
        str_from_chars += b
    return str_from_chars


def xor_binary(a, b, n):
    """
    Function Xor
    :param a: binary 1
    :param b: binary 2
    :param n: length of the binary
    :return: xor binary
    """
    ans = ""
    # Loop to iterate over the
    # Binary Strings
    for i in range(n):

        # If the Character matches
        if a[i] == b[i]:
            ans += "0"  # 1
        else:
            ans += "1"  # 0
    return ans


def transform_binary_to_text(message):
    """
    Example:
     01000001011011000110000101101001011011100010000001010100011000010111000001110000
     ==
     "Alain Tapp"
    :param message: binary message to convert
    :return: message
    """
    step1 = convert_binary_to_list_of_8bits(message)
    step2 = convert_binarylist_to_integer(step1)
    step3 = convert_integer_to_char(step2)
    step4 = concat_strings(step3)

    return step4


def convert_string_to_char(string):
    """
    Convert a string to a list of chars
    Example: “Alain Tapp” = [A,l,a,i,n,_,T,a,p,p]
    :param string: String to coonvert to Char
    :return: list of chars
    """
    list_char = []
    for element in string:
        list_char.append(element)
    return list_char


def convert_list_of_char_to_binary(list_char):
    """
    Create a liste of binary from a list of chars
    :param list_char: list to convert to binary
    :return: list of binary numbers (8 bits)
    """
    list_binary = []
    for char in list_char:
        list_binary.append(convert_integer_to_8bits(char))
    return list_binary


def convert_integer_to_8bits(letter):
    """
    Convert letter to an 8 bits binary
    Example: 'a' == '01000001'
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


def verify_if_word_is_french(word, letters):
    """
    Verify if a word includes all the french letters and spaces
    :param word: word to verify
    :param letters: list of letters in the alphabet
    :return: boolean
    """
    for ch in word:
        if ch not in letters:
            return False
    return True


def split_xored_message_with_word_length(message, word, position):
    return message[position:position + len(word)]


def decipher(xored_message_binary, word, letters):
    accepted_temp = []
    #accepted = []
    position = 0
    word_binary = concat_strings(convert_list_of_char_to_binary(convert_string_to_char(word)))
    word_length = len(word_binary)
    xor_length = len(xored_message_binary)
    for i in range(0, xor_length - word_length, 8):
        temp = split_xored_message_with_word_length(xored_message_binary, word_binary, position)
        temp_word = transform_binary_to_text(xor_binary(temp, word_binary, word_length))
        verify = verify_if_word_is_french(temp_word, letters)
        if verify:
            accepted_temp.append(temp_word)
            accepted_temp.append(position)
            print(accepted_temp)
            accepted_temp = []
        position += 8


def main():
    ##
    message_without_line_breaks = ""
    file_name_m = "message.txt"

    try:
        file = open(file_name_m, 'r')
    except FileNotFoundError:
        print('Pas de fichier.')
    else:
        for line in file:
            line_stripped = line.rstrip()
            message_without_line_breaks += line_stripped
        file.close()

    # split the message in 2 parts, M1 and M2
    m1 = message_without_line_breaks[:len(message_without_line_breaks) // 2]
    m2 = message_without_line_breaks[len(message_without_line_breaks) // 2:]

    #  (M1 xor k) xor (M2 xor k) = M1 xor M2
    xored_b = xor_binary(m1, m2, len(m1))

    accepted_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
                        'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                        'V', 'W', 'X', 'Y', 'Z', 'à', 'é', ' ', ',', '.', 'ê', 'è', 'î', "'", 'ï', 'ç']


    word = " comme " #['a tête ', 17328] ['rait en', 16552]

    #word = " homme est rouge comme une tomate tr" #[" sont debout, sauf l'homme à la ", 41888]
    #word = "Tous sont debout, sauf l'homme à la " #[' est rouge comme une tomate tr', 41904]
    #word = "Tous sont debout, sauf l'homme à la tête de Rouget "
    #word = " femme " #['r, pas ', 34704] ['t deuil', 27504]
    #word = " pas d' "

    #word = "Une mère à tête de morte montrait en riant sa fille à tête d'orpheline au vieux diplomate ami de la famille qui s'était fait la tête de Soleilland."
    decipher(xored_b, word, accepted_letters)



main()

# x = ['01000001', '01101100', '01100001', '01101001', '01101110',
#                         '00100000', '01010100', '01100001', '01110000', '01110000']
# y = convert_binarylist_to_integer(x)
# print(y)
# z = convert_integer_to_char(y)
# print(z)

# print(xor_binary('1000','1100',4))
