
list1 = (1, 2, 3, 4, 5)
list2 = (1, 2, 3, 4, 5)
asdf = zip(list1, list2)
print(list(asdf))

test_list = [12, 63535, 34, 3, 56767, 424, 232, 5, 7, 7, 8, 5, 7, 7, 7, 5, 7, 7]
item = 5

first_oc = test_list.index(5)
res = [i for i in test_list if i != item]
print(res, first_oc)

s = 20
print(f"this is : {s}")
