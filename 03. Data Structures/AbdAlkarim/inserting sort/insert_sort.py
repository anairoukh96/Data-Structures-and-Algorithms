def insertionSort(lst):
    for i in range(1, len(lst)):
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]
            k -= 1
        lst[k + 1] = currentElement

def main():
    list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    insertionSort(list)
    for v in list:
        print(v, end=" ")
main()