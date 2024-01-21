number_dictionary = {
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'}


def number_printer(in_string):
    temp_str = ''
    string_list = list(in_string)
    for element in string_list:
        temp_str = temp_str + number_dictionary[element] + ' '
    print(temp_str)

if __name__ == "__main__":
    in_string = input("Enter a string: ")
    number_printer(in_string)
