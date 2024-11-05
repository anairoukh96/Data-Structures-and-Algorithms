# list1=[2,3,5,2,33,21]

# i = 0
# while i < len(list1):
#     print(list1[i], end=" ")
#     i += 1

######################################################

list1 = [x for x in range(0,1000000)]
print(list1)

list2 = [0.5 * x for x in list1]
print(list2)

list3 = [x for x in list2 if x < 1.5]
print(list3)