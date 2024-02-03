import sys

if __name__ == "__main__":
    f1_name = sys.argv[1]
    f2_name = sys.argv[2]
    
    f1 = open(f1_name,"r")
    lines = f1.readlines()
    f1.close()

    f2 = open(f2_name,"w")
    f2.writelines(lines)
    f2.close()
