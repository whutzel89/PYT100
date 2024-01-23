def pos_list(in_list):
    return [abs(element) for element in in_list]

if __name__ == "__main__":
    abs_list = pos_list([1,2,3,4,-1,4,-5,-7])
    print(abs_list)
