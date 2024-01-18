def list_printer(input_string):
    number_list = list(input_string.split(','))
    for element in number_list:
        if int(element) > 0:
            print(element)

if __name__ == "__main__":
    input_string = input("Enter a string delimited with , no spaces: ")
    list_printer(input_string)
