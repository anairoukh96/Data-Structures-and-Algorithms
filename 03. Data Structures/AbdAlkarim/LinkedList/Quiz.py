from LinkedList import LinkedList
lstquiz = LinkedList()
lstquiz.addFirst("B")
lstquiz.add("i")
lstquiz.add("t")
lstquiz.add("c")
lstquiz.add("o")
lstquiz.add("i")
lstquiz.addLast("n")


for e in lstquiz:
    print(e, end = ' ')
print()

iterator = iter(lstquiz) # Create an iterator
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
