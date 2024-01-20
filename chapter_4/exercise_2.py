if __name__ == "__main__":
    new_words = set()
    temp_string = ''
    while True:
        data = input("enter a line (q to quit): ")
        if data == 'q':
            break
        temp_string = temp_string +data + ' '   
    new_words.update(sorted(temp_string.split(' '))[1:])
    print("This is the new set of sorted data: ",sorted(new_words))
    print("The length of the set is: ",len(new_words))
