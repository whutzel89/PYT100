def line_printer():
    print(repr(0).rjust(2), end=' ')
    for i in range(1,50):
        if i%10 == 9:
            print(repr(i).rjust(2))
        else:
            print(repr(i).rjust(2),end=' ')

if __name__ == "__main__":
    line_printer()
