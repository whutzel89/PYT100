

if __name__ == "__main__":
    in_string = "eEeEeEeE."
    #in_string = input("enter a string: ")
    print(in_string)
    new = in_string.replace('e','E')
    print("This strinh ends with .: "+str(in_string.endswith('.')))
    print(new[-1])
    print("This string is alphanumeric: "+ str(in_string.isalnum()))
