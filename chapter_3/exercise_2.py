def number_summer(a,b):
    sum = 0
    if a>b:
        for i in range(b,a+1):
            sum+=i
        print("sum is: "+str(sum))
    elif b>a:
        for i in range(a,b+1):
            sum+=i
        print("sum is: "+str(sum))
    else:
        print("sum is: "+str(a))


if __name__ == "__main__":
    number_summer(-4,1)
