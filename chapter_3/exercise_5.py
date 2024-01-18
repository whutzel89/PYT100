def line_printer():
    for i in range(0,50):
        if i%10 == 9:
            print(repr(i).rjust(2))
        else:
            print(repr(i).rjust(2),end=' ')

if __name__ == "__main__":
    line_printer()
