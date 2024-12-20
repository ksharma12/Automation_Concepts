import time
from abc import ABC, abstractmethod
from argparse import Action

from multipledispatch import dispatch
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://www.google.com/")
# print(driver.find_element(By.XPATH, "//img[@alt='Google']").get_property("alt"))
# print(driver.find_element(By.XPATH, "//img[@alt='Google']").get_attribute("alt"))
# driver.quit()

# driver = webdriver.Chrome()
# driver.get("https://www.amazon.in/")
# time.sleep(10)
# ele = driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']")
# action = ActionChains(driver)
# action.move_to_element(ele).perform()
# driver.find_element(By.XPATH, "//div[@id='nav-flyout-ya-signin']//span[@class='nav-action-inner'][normalize-space()='Sign in']").click()
# time.sleep(5)


print("-------------------------------------------args-----------------------------------")


def argsMyFunc(*abc):
    for n in abc:
        print(n)


argsMyFunc("asdf", "qwer", "zxcv", "uiop", "hjkl", "vbnm")
print("-------------------------------------------args---with--params--------------------------------")


def argsMyFunc_with_params(a1, a2, *args):
    for n in args:
        print(a1, a2, n)


argsMyFunc_with_params("My Caty", 234, "A", "B", "C", "D", "E")
print("-------------------------------------------Kwargs-----------------------------------------")


def kwargsMyFunc(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


kwargsMyFunc(One=1, Two=2, Three=3, Four=4)
print("----------------------------------Kwargs---with---arguments-------------------------------")


def kwargsMyFunc_with_params(arg1, arg2, **kwargs):
    for k, v in kwargs.items():
        print(k, v, arg1, arg2)


kwargsMyFunc_with_params("Hundred", 100, One=1, Two=2, Three=3, Four=4)
print("--------------------------args---Kwargs---with---arguments-------------------------------")


def args_kwargsMyFunc_with_params(arg1, arg2, *args, **kwargs):
    for n in args:
        print(arg1, arg2, n)
    for k, v in kwargs.items():
        print(k, v, arg1, arg2)


args_kwargsMyFunc_with_params("Thousand", 1000, "A", "B", "C", One=1, Two=2, Three=3, Four=4)

print("----------------------------lamda--expressions-----------------------------------------------------")
# lamda argument : expression (single expression multiple arguments)

x = lambda a: a + 1
print(x(5))

y = lambda a, b: a * b
print(y(5, 10))


# using lamda as anonymous function

def MyFunc(n):
    return lambda a: a * n


mydoubler = MyFunc(2)
print(mydoubler(3))
print(
    "------------------------------try , Except , Else , finally-----------------------------------------------------")

# try:
#     a = int(input("Enter the first number "))
#     b = int(input("Enter the second number "))
#     c = a / b
#     print(f"final result is {c}")
# except (ZeroDivisionError, ValueError):
#     print("error occurred in file")
#     print("please enter a valid number")
# else:
#     print("closing file")
# finally:
#     print("I will always executed")
# print("Out of try/Except block")
print("------------------------------Access Specifiers-----------------------------------------------------")


class A:
    a_public = "a_class_public_variable"
    _a_protected = "a_class_protected_variable"
    __a_private = "a_class_private_variable"

    def __init__(self):
        print("A class constructor")

    def a_public_method(self):
        print("This is a_class_public_method")

    def _a_protected_method(self):
        print("This is a_class_protected_method")

    def __a_private_method(self):
        print("This is a_class_private_method")


class B(A):
    def a_class_items(self):
        print(self.a_public)
        print(self.a_public_method())
        print(A._a_protected)
        print(A._a_protected_method(self))


b = B()
b.a_class_items()
print("------------------------------Abstract Class and Methods-----------------------------------------------------")


class Abstract(ABC):

    @abstractmethod
    def abstract_1(self, a, b):
        pass


class C(Abstract):

    def abstract_1(self, asdf, qwer):
        print(f"this is abstract 1 method with 2 argument, {asdf}, {qwer}")

    def c1(self):
        print("this is c1 method")


c = C()
c.abstract_1("Keshav", "Sharma")

print("-------------------------Operator----Overloading------------------------------------------------")


class OperatorOverload():
    def __init__(self, pages):
        self.pages = pages
        print("This is constructor", pages)

    def __add__(self, other):
        total_pages = self.pages - other.pages
        return total_pages


obj_1 = OperatorOverload(10)
obj_2 = OperatorOverload(20)

print("-------------------------Method----Overloading------------------------------------------------")

# class MethodOverloading:
#
#     def __init__(self):
#         print("asdf")
#
#     def __init__(self, a):
#         print("qwer")
#     def add(self, a, b):
#         print(a + b)
#
#     def add(self, a, b, c):
#         print(a + b + c)
#
#
# m = MethodOverloading("a")
# m.add(10, 10)
# m.add(10, 10, 10)

print("-------------------------Method/Constructor----Overriding------------------------------------------------")


class D:

    def __init__(self):
        print("constructor of class D")

    def de(self):
        print("method of D class")


class E(D):
    def __init__(self):
        super().__init__()
        print("E class constructor")

    def de(self):
        super().de()
        print("method of E class")


e = E()
e.de()

print("-----------------------class/instance/static----method/variables---------------------------------")


class F:
    f = 10  # class var

    def __init__(self, f_name, l_name):
        self.f_name = f_name  # instance variable
        self.l_name = l_name  # instance variable

    def f1(self):
        print("method of class f")

    @classmethod
    def f2(cls):
        print("class method of class f")

    @staticmethod
    def f3():
        print("static method of class f")


f = F("Keshav", "Sharma")
f.f1()
f.f2()
f.f3()

print("-----------------Method----Overloading-----------------------------------------------------------")


class G:
    @dispatch(int, int)
    def g1(self, a, b):
        print(a + b)

    @dispatch(int, int, int)
    def g1(self, a, b, c):
        print(a + b + c)

    @dispatch(float, float, int)
    def g1(self, a, b, c):
        print(a + b + c)


g = G()
g.g1(2, 3, 4)
g.g1(2, 3)
g.g1(2.6, 3.3, 4)

print("------------------------------------Inheritance--------------------------------------------------")


class H:

    def __init__(self):
        print("H class constructor")

    def common(self):
        print("H class common function")

    def h(self):
        print("H class h function")


class I(H):

    def __init__(self):
        H.__init__(self)
        print("I class constructor")

    def common(self):
        print("I class common function")

    def common_i_j(self):
        print("I class common I_J function")

    def i(self):
        print("I class i function")


class J:

    def __init__(self):
        print("J class constructor")

    def common(self):
        print("J class common function")

    def common_i_j(self):
        print("J class common I_J function")

    def j(self):
        print("J class j function")


class K(J, I):

    def __init__(self):
        J.__init__(self)
        I.__init__(self)
        print("k class constructor")

    def common(self):
        print("K class common function")

    def k(self):
        print("K class k function")


k = K()
k.common()
k.common_i_j()
k.h()
k.i()
k.j()

print("--------------------------Sets---------------------------------------------------------------")

s1 = {"One", 1, 1.1, True}
s2 = {"Two", 2, 2.2, False}
s3 = {"Three", 3, 3.3, True, 3, "Three", True}

print(type(s1))
print(len(s1))

for ele in s1:
    print(ele)

print(s3)

s1.add(11.1)
print(s1)

s1.remove(11.1)

print(s1)

s1.discard(1.1)
print(s1)

s3 = {1, 2, 3, 4, 5, 5}
s4 = {6, 7, 8, 9, 10}

s3.update(s4)
print(s3)

s5 = {"Keshav", "Sharma"}
s6 = s3.copy()
print(s6)

s3.clear()
print(s6)

print("--------------------------Dictionary---------------------------------------------------------")

d1 = {"one": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
d2 = {"six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10}

d3 = {"Eleven": 11, "Twelve": 12, "Thirteen": 13, "Fourteen": 14, "Fifteen": 15}

print(type(d1))
print(len(d1))
print(d1.values())
print(d1.keys())
print(d1.items())
print(d1.get("Three"))
print(d1["Four"])

del d3["Fifteen"]
print(d3)

for n in d1.items():
    print(n)
for n in d1.keys():
    print(n)
for n in d1.values():
    print(n)

print("-----------------------------------------------------------------------------------------------")

d4 = {
    "l1": [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    "d1": {"one": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5},
    "s1": {"six", "Seven", "Eight", "Nine", "Ten"},
    "t1": (6, 7, 8, 9, 10)
}

print(d4["l1"][4])
print(d4["d1"]["Three"])
print(d4["s1"])
print(d4["t1"][4])

print("------------------------------Dictionary Comprehension-----------------------------------------")

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 6, 6, 6, 4, 3, 3, 3, 4]
print({n: lst.count(n) for n in lst})

print("-------------------------------Tuples---------------------------------------------------------")

t1 = ("One", 2, 3.3, True, "Keshav", 5, "Six", 7, "Eight")
t2 = ("Nine", 10, 11.11, False, "Sharma", 12, "Thirteen", 14, "Fifteen")
print(type(t1))

print(t1[:])
print(t1[3:])
print(t1[:4])
print(t1[3:5])

print(t1 * 2)
print(t1 + t2)

t3 = t1[:]
print(t3)

print("--------------------------------------list---------------------------------------------------")

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(type(l1))
l2.append("Keshav")
print(l1)

print(f"a land is so {l1[3]} deep that is {l1[5]}")
print(l1[:])
print(l1[3:])
print(l1[:4])
print(l1[3:5])
print(l1[::-1])
print(l1[0:8:2])

l1.sort()
l1.sort(reverse=True)

print(l1)

a = 10
b = 3

print(a ** b)

print("---------------------------------------------Questions---------------------------------------")

# reverse order and reverse words in a string
a_reverse_0_13 = "sniatnuom yawa raf tsae eht ni sesir nuS"
print(a_reverse_0_13[::-1])

# same order but reverse words in a string
a_reverse_1_13 = "nuS sesir ni eht tsae raf yawa sniatnuom"
print(" ".join([n[::-1] for n in a_reverse_1_13.split(" ")]))

# same words but reverse order in a string
a_reverse_2_13 = "mountains away far east the in rises Sun"
print(" ".join(n for n in a_reverse_2_13.split(" ")[::-1]))

ques_1_1 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
ques_1_2 = [6, 7, 8, 9, 0, 0, 9, 8, 7, 6]

ques_1_3 = (1, 2, 3, 4, 5, 5, 4, 3, 2, 1)
ques_1_4 = (6, 7, 8, 9, 0, 0, 9, 8, 7, 6)

ques_1_5 = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
ques_1_6 = {6, 7, 8, 9, 0, 0, 9, 8, 7, 6}
asdf = list(zip(ques_1_1, ques_1_2))
print(asdf)
print(asdf[3][1])

# Q2 Find the Count of chars with respect to chars
list2 = ['a', 'b', 'c', 'd', 'a', 'c', 'd', 'b', 'b', 'a']
print({n: list2.count(n) for n in list2})

# Q3 Remove all elements which are duplicate in the list
ques_3 = ['a', 'b', 'c', 'd', 'a', 'a']
print([n for n in ques_3 if ques_3.count(n) == 1])

# Q4 Remove all elements which are duplicate in the list except 1
list4 = ['a', 'b', 'c', 'd', 'a', 'a']
list(set(list4)).sort()
print(list4)

# Q9 Multiply each corresponding elements of 2 lists of same length and return a list
ques_9_1 = [2, 3, 4, 5]
ques_9_2 = [6, 7, 8, 9]
print([x * n for x, n in zip(ques_9_1, ques_9_2)])

# Q11 Multiply each element to each element of 2 lists of different/same length and return a list
ques_11_1 = [2, 3, 4, 5]
ques_11_2 = [6, 7, 8]

print([x * n for n in ques_11_1 for x in ques_11_2])

# Q12 Print the pattern as list : ab , aabb, aaabbb, aaaabbbb, .....
n = 5
print(["a" * n + "b" * n for n in range(1, n + 1)])

# Q13 Print the pattern as list : ab , abb, abbb, abbbb, .....
n = 5
print(["a" + "b" * n for n in range(1, n + 1)])

# Q14 Add each element index of the list 2 its value
ques_14 = [13, 14, 15, 16, 17, 18, 19, 20]
print([i + n for i, n in enumerate(ques_14)])

# Q15 Multiply each pair of 2 list (index and value) and make a single list
ques_15_1 = [13, 14, 15, 16, 17, 18, 19, 20]
ques_15_2 = [21, 22, 23, 24, 25, 26, 27, 28]

print([i * n for i, n in enumerate(zip(ques_15_1, ques_15_2))])

# Q16 Write down a dictionary with keys as addition of indexes of 2 lists corresponding to
# their values as multiplication of their items
ques_16_1 = [3, 1, 5, 8]
ques_16_2 = [2, 4, 6, 7]

print({ques_16_1.index(v1) + ques_16_2.index(v2): v1 * v2 for v1, v2 in zip(ques_16_1, ques_16_2)})
