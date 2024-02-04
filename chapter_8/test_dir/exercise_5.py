def sort(var):
    temp = list(var)
    return sorted(var)
    
def reverse(var):
    temp = list(var)
    return list(reversed(var))

if __name__ == "__main__":
    values = [10,2,50,45,1]
    print(sort(values))
    print(reverse(values))
    print(reverse(sort(values)))
