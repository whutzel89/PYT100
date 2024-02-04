import sys

if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    file3 = sys.argv[3]
    file4 = sys.argv[4]

    f1 = open(file1,'r')
    f2 = open(file2,'r')
    f3 = open(file3,'r')
    f4 = open(file4,'r')

    lines = []
    new_lines = []

    lines.append(f1.readlines())
    lines.append(f2.readlines())
    lines.append(f3.readlines())
    lines.append(f4.readlines())

    for x in lines:
        for ele in x:
            new_lines.append(ele)
    elements = set(new_lines)

    for element in elements:
        print(element+' has occured: '+str(new_lines.count(element)))
