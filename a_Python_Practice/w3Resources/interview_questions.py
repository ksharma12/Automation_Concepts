lst = [2, 4, 3, 5, 6, 5, 8, 7, 5, 3, 2, 6, 8, 7, 5, 3, 2, 1, 5]
itm = 5


# remove duplicates from the list
def remove_duplicates(test_list, item):
    res = [i for i in test_list if i != item]
    return res


s1 = "$100"
s2 = "$5.5"
expected_result = "$105.5"

new_s1 = int(s1.split("$")[1])
new_s2 = float(s2.split("$")[1])
result = new_s1 + new_s2
final_result = "$" + str(result)
print(final_result)


