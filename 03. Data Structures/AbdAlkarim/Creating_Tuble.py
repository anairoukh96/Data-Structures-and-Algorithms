# Tuple

# t1 = ()

# t2 = (1, 3, 5)

# print("t2 = ",t2)

# t3 = tuple([2 * x for x in range(1,5)])
# print("t3 = ",t3)

# t4 = tuple("abcd")
# print("t4 = ",t4)

# t5 = t2 + t3 + t4
# print("t5 = ",t5)

# Set


# s1 = set()

# s2 = {1, 3, 5}
# print("s2 = ",s2)

# s3 = set([1, 3, 5])
# print("s3 = ",s3)

# s4 = set([x * 2 for x in range(1, 10)])
# print("sum s4 = ",sum(s4))
# print("len s4 = ",len(s4))
# print("max s4 = ",max(s4))
# print("min s4 = ",min(s4))
# print("avg s4 = ",sum(s4)/len(s4))

# s5 = set("abcd")
# print("s5 = ",s5)

# s6 = s5 + s4 + s3 + s2
# print(s6)

# s7 = t5 + s6
# print(s7)

# اتحاد
s1 = {1, 2, 4}
s2 = {1, 3, 5}
print(s1.union(s2))
print(s1 | s2)

# تقاطع
s1 = {1, 2, 4}
s2 = {1, 3, 5}
print(s1.intersection(s2))
print(s1 & s2)



