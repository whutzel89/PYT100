if __name__ == "__main__":
    new_words = set()
    temp_string = ''
    word_dict = {}
    while True:
        data = input("enter a line (q to quit): ")
        if data == 'q':
            break
        temp_string = temp_string +data + ' '   
    new_words.update(sorted(temp_string.split(' '))[1:])
    for element in sorted(new_words):
        word_dict[element] = temp_string.split(' ').count(element)

    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    for key in sorted(word_dict.keys()):
        print('the word %s occurs %s times' % (key,word_dict[key]))

    print('+++++++++++++++++++++++++++++++++++++++++++++++++')
    val_dict = {k:v for k, v in sorted(word_dict.items(), key=lambda item: item[1])}
    for key in val_dict.keys():
        print('the word %s occurs %s times' % (key,val_dict[key]))

