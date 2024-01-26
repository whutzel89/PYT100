def main_fun(c,d):
    a =c
    b=d
    def sub_fun(a,b):
       return a +b
    return sub_fun

if __name__ == "__main__":
    var = main_fun(5,2)
