def print_numbers(input_string):
    low,high,step = input_string.split(',')
    for ele in range(int(low),int(high)+1,int(step)):
        print(ele)

if __name__ == "__main__":
    input_string = input('Input a string delmited by , (low, high, step): ')
    print_numbers(input_string)
