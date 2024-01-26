def shared_ele(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 & set2

if __name__ == "__main__":
    temp1 = [1,2,3,4,5,6,7]
    temp2 = [9,8,7,6,5,4,3]
    print(shared_ele(temp1,temp2))
