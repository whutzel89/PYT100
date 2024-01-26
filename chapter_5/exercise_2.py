def num_counter(*nums,num=0):
    counts = 0
    for count in nums:
        if count > num:
            counts+=1
    return counts

if __name__ == "__main__":
    var = num_counter(1,2,34,5,10,num= 10)
    print(var)
