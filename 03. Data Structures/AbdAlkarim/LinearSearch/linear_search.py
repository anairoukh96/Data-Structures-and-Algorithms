def linearSearch(lst, key):
    for i in range(0 , len(lst)):
        if key == lst[i]:
            return i
    return -1
list1 = [2,3,5,7]
print(linearSearch(list1,5))