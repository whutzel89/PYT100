if __name__ == "__main__":
    list_ten = [0,1,2,3,4,5,6,7,8,9]
    cin = ''
    while cin != 'end':
        cin = input('Enter numer 0 - 9:')
        try:
            cin = int(cin)
            print(list_ten[cin])
        except:
            print('an error has occured')
