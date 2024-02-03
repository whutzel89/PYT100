import sys

if __name__ == "__main__":
    f1_name = sys.argv[1]
    f2_name = sys.argv[2]
    try:
        f1 = open(f1_name,"r")
        f2 = open(f2_name,"r+")
    except OSError:
        print('Read file does not exist')
        sys.exit()

    lines = f1.readlines()
    f1.close()
    f2.writelines(lines)
    f2.close()
