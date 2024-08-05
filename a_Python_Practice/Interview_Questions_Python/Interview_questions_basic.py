# Q1 Join 2 tuples, lists, sets and dictionaries together with zip function
import itertools

ques_1_1 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
ques_1_2 = [6, 7, 8, 9, 0, 0, 9, 8, 7, 6]

ques_1_3 = (1, 2, 3, 4, 5, 5, 4, 3, 2, 1)
ques_1_4 = (6, 7, 8, 9, 0, 0, 9, 8, 7, 6)

ques_1_5 = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
ques_1_6 = {6, 7, 8, 9, 0, 0, 9, 8, 7, 6}

ques_1_7 = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
ques_1_8 = {6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
ques_1_9 = {6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

print("Q1.1 : ", list(zip(ques_1_1, ques_1_2)))  # 2 lists -> list
print("Q1.2 : ", list(zip(ques_1_2, ques_1_3)))  # list and tuple -> list
print("Q1.3 : ", list(zip(ques_1_3, ques_1_4)))  # 2 tuples -> list
print("Q1.4 : ", list(zip(ques_1_4, ques_1_5)))  # tuple and set -> list
print("Q1.5 : ", list(zip(ques_1_5, ques_1_6)))  # 2 sets -> list
print("Q1.6 : ", list(zip(ques_1_1, ques_1_6)))  # list and set -> list

print("Q1.7 : ", tuple(zip(ques_1_1, ques_1_2)))  # 2 lists -> tuple
print("Q1.8 : ", tuple(zip(ques_1_2, ques_1_3)))  # list and tuple -> tuple
print("Q1.9 : ", tuple(zip(ques_1_3, ques_1_4)))  # 2 tuples -> tuple
print("Q1.10 : ", tuple(zip(ques_1_4, ques_1_5)))  # tuple and set -> tuple
print("Q1.11 : ", tuple(zip(ques_1_5, ques_1_6)))  # 2 sets -> tuple
print("Q1.12 : ", tuple(zip(ques_1_1, ques_1_6)))  # list and set -> tuple

print("Q1.13 : ", set(zip(ques_1_1, ques_1_2)))  # 2 lists -> set
print("Q1.14 : ", set(zip(ques_1_2, ques_1_3)))  # list and tuple -> set
print("Q1.15 : ", set(zip(ques_1_3, ques_1_4)))  # 2 tuples -> set
print("Q1.16 : ", set(zip(ques_1_4, ques_1_5)))  # tuple and set -> set
print("Q1.17 : ", set(zip(ques_1_5, ques_1_6)))  # 2 sets -> set
print("Q1.18 : ", set(zip(ques_1_1, ques_1_6)))  # list and set -> set

print("Q1.19 : ", list(zip(ques_1_7.values(), ques_1_8.values())))  # 2 dic values -> list
print("Q1.20 : ", set(zip(ques_1_7.keys(), ques_1_8.values())))  # 1 dic keys and 1 dic values -> set
print("Q1.21 : ", tuple(zip(ques_1_7.keys(), ques_1_8.keys())))  # 2 dic keys -> tuple
print("Q1.22 : ", set(zip(ques_1_8.keys(), ques_1_9.keys())))  # 2 same dic -> set

# Q2 Find the Count of chars with respect to chars
list2 = ['a', 'b', 'c', 'd', 'a', 'c', 'd', 'b', 'b', 'a']
print("Q2 : ", {n: list2.count(n) for n in list2})

# Q3 Remove all elements which are duplicate in the list
ques_3 = ['a', 'b', 'c', 'd', 'a', 'a']
duplicate_item = 'a'
print("Q3.1 : ", [n for n in ques_3 if n != duplicate_item])
ques_3_1 = [n for n in ques_3 if ques_3.count(n) != 1]
print("Q3.2 : ", [x for x in ques_3 if x not in ques_3_1])

# Q4 Remove all elements which are duplicate in the list except 1
list4 = ['a', 'b', 'c', 'd', 'a', 'a']
duplicate_item = 'a'
print("Q4 : ", list((set(list4))))

# Q5 Write a palindrome of string
ques_5 = "madam"
print("Q5 : ", ques_5[::-1])

# Q6 Reverse words spelling and reverse order of words in a string
ques_6 = "Sun rises in the east far away mountains"
ques_ans_6 = "sniatnuom yawa raf tsae eht ni sesir nuS"
print("Q6 : ", ques_6[::-1])

# Q7 Reverse words spelling and fixed words position in a string
ques_7 = "Sun rises in the east far away mountains"
ques_ans_7 = "nuS sesir ni eht tsae raf yawa sniatnuom"
print("Q7 : ", " ".join([n[::-1] for n in ques_7.split()]))

# Q8 Same words spelling and reverse words order in a string
ques_8 = "Sun rises in the east far away mountains"
ques_ans_8 = "mountains away far east the in rises Sun"
print("Q8.1 : ", " ".join([n for n in ques_8.split()[::-1]]))
print("Q8.2 : ", " ".join((reversed(ques_8.split()))))

# Q9 Multiply each corresponding elements of 2 lists of same length and return a list
ques_9_1 = [2, 3, 4, 5]
ques_9_2 = [6, 7, 8, 9]
print("Q9.1 : ", [x * n for n, x in zip(ques_9_1, ques_9_2)])
print("Q9.2 : ", [ques_9_1[n] * ques_9_2[n] for n in range(len(ques_9_1))])

# Q10 Multiply each corresponding elements of 2 lists of different length and return a list
ques_10_1 = [2, 3, 4, 5]
ques_10_2 = [6, 7, 8]
ques_10_3 = [9, 10, 11, 12]
print("Q10.1 : ", [ques_10_1[n] * ques_10_2[n] for n in range(len(ques_10_2))])  # mandatory to choose small length list
print("Q10.2 : ", [x * n for n, x in zip(ques_10_2, ques_10_1)])  # iteration happened till the smallest exhausted

# Q11 Multiply each element to each element of 2 lists of different/same length and return a list
ques_11_1 = [2, 3, 4, 5]
ques_11_2 = [6, 7, 8]
ques_11_3 = [9, 10, 11, 12]
print("Q11.1 : ", [x * n for x in ques_11_2 for n in ques_11_1])
print("Q11.2 : ", [x * n for x in ques_11_1 for n in ques_11_3])

# Q12 Print the pattern as list : ab , aabb, aaabbb, aaaabbbb, .....
n = 5
print("Q12 : ", [n * "a" + n * "b" for n in range(1, n + 1)])

# Q13 Print the pattern as list : ab , abb, abbb, abbbb, .....
n = 5
print("Q13 : ", ["a" + n * "b" for n in range(1, n + 1)])

# Q14 Add each element index of the list 2 its value
ques_14 = [13, 14, 15, 16, 17, 18, 19, 20]
print("Q14 : ", [index + value for index, value in enumerate(ques_14)])

# Q15 Multiply each pair of 2 list (index + value) and make a single list
ques_15_1 = [13, 14, 15, 16, 17, 18, 19, 20]
ques_15_2 = [21, 22, 23, 24, 25, 26, 27, 28]
print("Q15 : ", [index * value for index, value in enumerate(zip(ques_15_1, ques_15_2))])

# Q16 Write down a dictionary with keys as addition of indexes of 2 lists corresponding to
# their values as multiplication of their items
ques_16_1 = [3, 1, 5, 8]
ques_16_2 = [2, 4, 6, 7]
print("Q16 : ", {ques_16_1.index(v1) + ques_16_2.index(v2): v1 * v2 for v1, v2 in zip(ques_16_1, ques_16_2)})

# Q17 Print a text / string n number of times in single line with another string / space in between
ques_17 = "Keshav"
ques_ans_17 = "Keshav Keshav Keshav Keshav Keshav"
print("Q17 : ", " ".join(ques_17.split() * 5))

# Q18 Multiply corresponding keys and values of 2 dictionary and create a new dictionary
ques_18_1 = {1: 11, 2: 12, 3: 13}
ques_18_2 = {4: 14, 5: 15, 6: 16}
print("Q18 : ",
      {k1 * k2: v1 * v2 for k1, k2, v1, v2 in
       zip(ques_18_1.keys(), ques_18_2.keys(), ques_18_1.values(), ques_18_2.values())})

# Q19 Create a dictionary with (index + key + value) as key and (index * key * value) as value
ques_19 = {1: 11, 2: 12, 3: 13, 4: 14, 5: 15}
print("Q19 : ", {index + key + value: index * key * value for index, (key, value) in enumerate(ques_19.items())})

# Q20 Nested list comprehension
ques_20_matrix = [[j for j in range(4)] for i in range(3)]
print(ques_20_matrix)

# Q21 Arrange 2 strings words alternately in a single string
ques_21_1 = "The of is but is"
ques_21_2 = "color snow white water colorless"
ans_21 = "The color of snow is white but water is colorless"
print(" ".join([a + " " + b for a, b in zip(ques_21_1.split(), ques_21_2.split())]))




