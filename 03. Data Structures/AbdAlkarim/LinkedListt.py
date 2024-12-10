def LinkedList():
    from LinkedList import LinkedList        # from اسم الملف  import اسم فانكشين
    lst = LinkedList()
    
    lst.add("Hebron")
    print("(1)", lst)

    lst.add("Ramallah")
    print("(2)", lst)

    lst.addLast("Nablus")
    print("(3)", lst)

    lst.addLast("Jenin")
    print("(4)", lst)
    
    lst.addLast("Tolkarm")
    print("(5)", lst)

    lst.addLast("Betlahim")
    print("(6)", lst)

LinkedList()