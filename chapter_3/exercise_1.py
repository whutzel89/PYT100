def number_compare(a,b):
    if a > b:
        print(str(a)+" is bigger than "+str(b))
    elif b>a:
        print(str(b)+" is bigger than "+str(a))
    else:
        print(str(a)+" is equal to "+str(b))
    return
    
if __name__ == "__main__":
    number_compare(5,4)
    number_compare(4,5)
    number_compare(5,5)
