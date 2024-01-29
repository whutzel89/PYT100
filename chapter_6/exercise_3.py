import sys

def sorter(param):
    return sorted(param)

def summer(param):
    return sum([int(x) for x in param])

if __name__ == "__main__":
    print(sorter(sys.argv[1:]))
    print(summer(sys.argv[1:]))
