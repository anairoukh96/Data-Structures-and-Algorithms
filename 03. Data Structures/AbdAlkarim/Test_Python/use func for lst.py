def name_example():
    print("1- List Compreshensions for Efficient Sequence Creation")
    print("2- List Compreshensions for Efficient Sequence Creation")
    print("3- Splitting a String to a List")
    print("4- Analyze Numbers")
    print("5- Pass By Value")
    print("6- Subtle Issues Regarding Default Arguments")
    print("7- Returning a List from a Function")
    print("8- Counting Occurrence of Each Letter")
    print("9- Linear Search Animation")
    print("10- Binary Search Animation")
def example_1():
    print("Example 1: List Compreshensions for Efficient Sequence Creation:\n")
    list1 = [x for x in range(0,5)]
    print("List 1 is: ",list1, "\n")
    list2 = [0.5 * x for x in list1]
    print("List 2 is list 1 * 0.5 result is: ", list2)
    list3 = [x for x in list2 if x < 1.5]
    print("if list 2 < 1.5 ... list 3 is: ", list3)
def example_2():
    print("Example 2: List Compreshensions for Efficient Sequence Creation:\n")
    list1 = ['green', 'red', 'blue']
    list2 = ['red', 'blue', 'green']
    print("List 1 = ",list1)
    print("List 2 = ",list2)
    print("List 1 == List 2 is: ",list1 == list2)
    print("List 1 != List 2 is: ",list1 != list2)
    print("List 1 >= List 2 is: ",list1 >= list2)
    print("List 1 > List 2 is: ",list1 > list2)
    print("List 1 < List 2 is: ",list1 < list2)
    print("List 1 <= List 2 is: ",list1 <= list2)
def example_3():
    print("Example 3: Splitting a String to a List:\n")
    items = "Welcome to the SCME".split()
    print("Welcome to the SCME with split is: ",items)
    items2 = "34#13#78#450".split("#")
    print("34#13#78#450 with split is: ",items2)
def example_4():
    print("Example 4: Analyze Numbers:\n")
    NUMBER_OF_ELEMENTS = 3  
    numbers = [] 
    sum = 0

    for i in range(NUMBER_OF_ELEMENTS): 
        value = float(input("Enter a new number: "))
        numbers.append(value)  
        sum += value
    
    average = sum / NUMBER_OF_ELEMENTS

    count = 0 
    for i in range(NUMBER_OF_ELEMENTS): 
        if numbers[i] > average:  
            count += 1

    print("Average is", average)
    print("Number of elements above the average is", count)
def example_5():
    print("Example 5: Pass By Value:\n")
    def main1():
        x = [1]
        y = [1, 2, 3]
        m(x, y)
        print("x[0] is " + str(x[0]))
        print("y[0] is " + str(y[0]))

    def m(number, numbers):
        number[0] = 1001
        numbers[0] = 5555
    main1()
def example_6():
    print("Subtle Issues Regarding Default Arguments:\n")
    def add(x, lst = []):
        if not(x in lst):
            lst.append(x)
        return lst
    list1 = add(1)
    print("List 1 = ", list1)
    list2 = add(2, [11, 12, 13, 14])
    print("List 2 = ", list2)
def example_7():
    print("Example 7: Returning a List from a Function:\n")
    def reverse(list):
        result = []
        for element in list:
            result.insert(0, element)
        return result
    list1 = [1,2,3,4,5,6]
    list2 = reverse(list1)
    print("List 1 is: ", list1)
    print("List 2 is: ", list2)
def example_8():
    print("Example 8: Counting Occurrence of Each Letter:\n")
    def count(s, c):
        res = 0
        for i in range(len(s)):
            if (s[i] == c):
                res = res + 1
        return res
    str = "geeksforgeeks"
    c = 'e'
    print("letter is: ", str)
    print("Letter search is: ", c)
    print("Counting number len letter is: ",count(str, c))
def example_9():
    print("Example 9: Linear Search Animation:\n")
    def linearSearch(lst, key):
        for i in range(0, len(lst)):
            if key == lst[i]:
                return i
        return -1
    list1 = [2,3,5,7]
    print(list1)
    print("len LinearSearch is: ",linearSearch(list1,5))
def example_10():
    print("Binary Search Animation\n")
    def binarySearch(lst, key):
        low = 0
        high = len(lst) - 1
        while high >= low:
            mid = (low + high) // 2
            if key < lst[mid]:
                high = mid - 1
            elif key == lst[mid]:
                return mid
            else:
                low = mid + 1
        return -low -1
    sorted_list = [3, 6, 9, 12, 15, 18, 21]
    key_to_find = 12
    print("Sorted list is = ", sorted_list)
    print("Key to find is = ", key_to_find)
    print("BinarySearch is: ", binarySearch(sorted_list, key_to_find))

def main():
    print("\nWelcome to the List Examples Program!\n")
    name_example()
    section_choice = int(input("Enter a number between 1 and 10 to run an example (or any other number to exit): "))
    if 1 <= section_choice <= 10:
        if section_choice == 1:
            example_1()
        elif section_choice == 2:
            example_2()
        elif section_choice == 3:
            example_3()
        elif section_choice == 4:
            example_4()
        elif section_choice == 5:
            example_5()
        elif section_choice == 6:
            example_6()
        elif section_choice == 7:
            example_7()
        elif section_choice == 8:
            example_8()
        elif section_choice == 9:
            example_9()
        elif section_choice == 10:
            example_10()
        else:
            print("Exiting the program. Goodbye!")
main()
