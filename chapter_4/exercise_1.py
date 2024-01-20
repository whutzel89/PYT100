def set_printer():
    in_set = set()
    out_set = set()
    t = 0
    number = input("enter a number (end to end): ")
    while number != 'end':
        if number in in_set:
            out_set.add(number)
        else:
            in_set.add(number)
        number = input("enter a number (end to end): ")

    print("elements in set: ",in_set)
    print("numbers not added set: ",out_set)
            
        
        

if __name__ =="__main__":
    set_printer()
