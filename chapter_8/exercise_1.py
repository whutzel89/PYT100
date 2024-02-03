if __name__ == "__main__":
    f1 = open('data.txt',"r")
    lines = f1.readlines()
    f1.close()

    f2 = open('empty.txt',"w")
    f2.writelines(lines)
    f2.close()
