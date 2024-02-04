if __name__ == "__main__":
    f1 = open('names_1.txt','r')
    f2 = open('names_2.txt','r')
    lines_1 = set(f1.readlines())
    lines_2 = set(f2.readlines())
    print("overlapping elemenets are: ",lines_1.intersection(lines_2))
