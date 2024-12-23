# 12/11/2024 Thusday
####################################################################################

def selectionSort(lst):
    for i in range(len(lst)-1):
        currentMin = min(lst[i : ])
        currentMinIndex = i + lst[i : ].index(currentMin)
        if currentMinIndex != i:
            lst[currentMinIndex], lst[i] = lst[i], currentMin
    return lst
list1 = [4,5,99,8,65,46,82,130,52]
print(selectionSort(list1))