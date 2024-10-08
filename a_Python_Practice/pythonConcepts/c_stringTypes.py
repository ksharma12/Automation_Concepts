print(type("this is string"))

a = "welcome to w2a"
print(a)

b = 'welcome to w2a'
print(b)

'''
hey my name is "Keshav Sharma"
'''

print('hey my name is "Keshav Sharma"')

e = "hey" \
    "my" \
    "name" \
    "is" \
    "Keshav" \
    "Sharma"

print(e)

g = """
hey 
my name is
keshav sharma
"""

print(g)

print("This is keshav's sharma \"new\" house")

# slicing the string
name = "keshav"
print(name[0])
print(name[4])
print(name[1:4])

# jumping steps
print(name[1:4:2])
print(name[::2])

# reversing the string
print(name[::-1])

print(len(name))

# all white spaces removed
abc_name = " hello, keshav    "
print(abc_name.strip())
print(abc_name.lower())
print(abc_name.upper())

b = abc_name.split(",")
print(b[0].strip())

# concatenation
ab = "hi"
cd = "Keshav Sharma"

# both type should be same for concatenation
print(ab + cd)

# repetition
print("10" * 6)

# as per BOD MASS rule, first multiplication and then addition
print("ba" + "na" * 2)

# string formatters
city = "Gurugram"
age = 31
id = 7.23
print("hey i live in", city)

# f-Strings
print(f"Hey i live in {city} and my age is {age} and my id is {id}")
# .format method
print("Hey i live in {} and my age is {} and my id is {}".format(city, age, id))
# % formatter
print("Hey i live in %s and my age is %d and my id is %f" % (city, age, id))

namoo = "asdfertgf"
print(namoo[1:10:2])

actual = "editor and run it"
reversal = 'rotide', 'dna', 'nur', 'ti'
lst = list(actual.split())
word = [n[::-1] for n in lst]
print(word)


namoo = "asdfertgf"
print(namoo[1:10:2])

a_string13 = "Sun rises in the east far away mountains"

# reverse order and reverse words in a string
a_reverse_0_13 = "sniatnuom yawa raf tsae eht ni sesir nuS"
a_reverse_0_13_solution = a_string13[::-1]
print("-------------------------------------------------------------------------------------------------")
print(a_string13)
print(a_reverse_0_13_solution)
print(a_reverse_0_13_solution == a_reverse_0_13)
print("-------------------------------------------------------------------------------------------------")

# same order but reverse words in a string
a_reverse_1_13 = "nuS sesir ni eht tsae raf yawa sniatnuom"
a_reverse_1_13_solution = " ".join([n[::-1] for n in a_string13.split()]).strip()
print("-------------------------------------------------------------------------------------------------")
print(a_string13)
print(a_reverse_1_13_solution)
print(a_reverse_1_13_solution == a_reverse_1_13)

# same words but reverse order in a string
a_reverse_2_13 = "mountains away far east the in rises Sun"
a_reverse_2_13_solution = " ".join(a_string13.split()[::-1]).strip()
print("-------------------------------------------------------------------------------------------------")
print(a_string13)
print(a_reverse_2_13_solution)
# print(a_reverse_2_13_solution == a_reverse_2_13)