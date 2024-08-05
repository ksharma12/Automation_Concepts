import math
import random


class A:
    # public variables (by default)
    a_string_variable = "My name is Keshav Sharma"  # string
    a_number_variable = 14  # numeric (integer)
    a_float_variable = 23.45  #
    a_complex_integer_variable = 34j
    a_complex_float_variable = 64.54j
    a_d = 10
    a_bool = False
    a_list = [23, 54, 6, 7, 6, "Keshav", "Aman", "Rahul", "Jyoti"]
    a_set = {"Keshav", "Keshav", 23, 23}
    a_set1 = set(["Keshav", "Keshav", 23, 23])
    a_frozenset = frozenset(["Keshav", "Keshav", 23, 23])
    a_tuple = (23, 54, 56, 98, 2, 7, "raghu", "rajeev", "anvar")
    a_dictionary = {"one": 1, "two": 2, 3: "three", 4: "four"}

    # protected variables (can be accessed within class and derived class)
    _a_d = 26  # private variable
    _a_A932432jsgg = "asdfff"
    _a_bool = True

    # private variable (can be accessed only within the class)
    __a_d = 44  # value cannot be overridden (final value)
    __a_var1, __a_var2, __a_var3 = "asdafaffaawa", 34, 22j

    def basic(self):
        print(round(math.pi))
        print(random.randrange(1, 100))
        # division always get floating number
        print(100 / 100)
        # without decimal
        print(100 // 100)
        # modulus
        print(11 % 3)
        print(3 ** 14)  # (base**power)/(3^14)

    def stringconcepts(self):
        a_string0 = "1234567890"
        a_string1 = "My Father was Food Inspector"
        a_string2 = 'My name is Keshav Sharma'
        a_string3 = '''The rainbow is "beautiful"'''
        a_string4 = '''There are 4 children outside'''
        a_string5 = "The" \
                    "color" \
                    "of" \
                    "water"
        a_string6 = """
                    hey 
                    my name is
                    keshav sharma
                    """
        a_string7 = """The stars are shining"""
        a_string8 = '''
        The
        Fumes
        are
        done
        '''
        a_string9 = "This is keshav sharma's \"new\" house"
        a_string10 = "   Dhole baje re baje re    "
        a_string12 = "  the    ,vinchi,code,mein,kuch,nahi,tha"

        # Thecolorofwater <class 'str'>
        print(a_string1, type(a_string1))
        print(a_string2, type(a_string2))
        print(a_string3, type(a_string3))
        print(a_string4, type(a_string4))
        print(a_string5, type(a_string5))
        print(a_string6, type(a_string6))
        print(a_string7)
        print(a_string8)
        print(a_string9)
        # including first index excluding last index
        # slicing string
        print(a_string1[0:11])
        print(a_string1[:8])
        print(a_string1[11:])
        print(a_string1[5])
        print(a_string0[0:10:2])  # gap of 1 between strings
        print(a_string0[1:10:2])  # # gap of 1 between strings
        print(a_string0[::2])  # gap of 1 between strings
        print(a_string0[::3])  # gap of 2 between strings
        print(a_string0[::1])  # gap of 0 between strings
        print(a_string0[::-1])  # reverse whole string
        print(len(a_string0))
        print(a_string10.strip())  # all white spaces removed from both ends
        print(a_string1.split("a"))
        print(a_string1.split())
        print(a_string1.count("a", 0))
        # string formating
        __fname = "Keshav"
        __lname = "Sharma"
        __class = "7th"
        __rollno = 21
        city = "Gurugram"
        age = 31
        id = 7.23
        # .format method
        a_string11 = "This is informed to you that {} {} class {} rollno {} is chemises"  # .format method
        print(a_string11.format(__fname, __lname, __class, __rollno))
        # f-string
        print(f"This is informed to you that {__fname} {__lname} class {__class} rollno {__rollno} is chemises")
        z = a_string12.split(",")
        # percentage formater
        print("Hey i live in %s and my age is %d and my id is %f" % (city, age, id))
        print(z)
        print(z[0].strip())
        print("alpha" + "beta" + "gama")  # concatination
        print("alpha " * 8)  # repetition
        # BODMAS rule brackets -> multiply -> Add
        print(("alpha " + "beta ") * 5)
        print("alpha " + "beta " * 3)
        print(a_string1.index("Foo"))
        print(a_string1.index("Fath", 3))
        print(a_string1.index("Fath", 3, 7))  # first index included last excluded
        print(a_string1.title())  # make each letter of word upper case in string
        print(a_string1.replace("Father", "Mother"))
        print(a_string1.join(" a "))
        print(" a ".join(a_string1))
        print(a_string1.upper())
        print(a_string1.lower())
        print(a_string1.capitalize())
        print((a_string1.upper().casefold() == a_string1.lower().casefold()))
        print(a_string1.upper().swapcase())  # printed as lower
        print(a_string1.lower().swapcase())  # printed as upper
        print(a_string1.count("F"))
        print(a_string1.center(50, "a"))
        txt = "My name is Ståle"
        x = txt.encode()
        print(x)
        print(txt.encode(encoding="ascii", errors="replace"))
        print(a_string1.endswith("or"))
        print(a_string1.find("Inspector"))
        txt1 = "H\te\tl\tl\to"
        x1 = txt1.expandtabs(10)
        print(x1)
        # input stored in variable a.
        a = {'x': 'John', 'y': 'Wick'}
        # Use of format_map() function
        print("{x}'s last name is {y}".format_map(a))
        a_string14 = "aaaaafor the welfare of societyaaaaa"
        print(a_string14.strip("a"))
        print(a_string14.lstrip("a"))
        print(a_string14.rstrip("a"))
        a_string15 = "a case the case for my case mia case down case lab"
        print(a_string15.rfind("case"))  # first occurrence of case from left
        print(a_string0.zfill(20))  # filled remaining spaces with 0s and other places with digits

        txt2 = "Good night Sam!"
        x2 = "mSa"
        y2 = "eJo"
        z2 = "odnght"
        mytable2 = str.maketrans(x2, y2, z2)
        print(txt2.translate(mytable2))
        print(a_string1.split("a"))
        print(a_string1.rsplit("a"))
        print(a_string1.splitlines(True))

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

    def flow_control_basics(self):
        a = 20
        b = 23
        if a > b:
            print("a is greater than b")
        elif a < b:
            print("b is greater than a")
        else:
            print("a is equal to b")

    def looping(self):
        for x in range(100):
            if x % 2 == 0 and x < 20:
                pass

        sequence = "Keshav Sharma"
        for x in sequence:
            print(f"The charracter present is {x} and the index is {sequence.index(x)}")

        for x in range(5, 15, 3):
            print(x)
        print("--------------------------------------")

        a = 2
        for x in range(1, 30, a):
            # a += 2
            print(x)

        print("--------------------------------------")

        i = 0
        while i < 10:
            print(i ** i)
            i += 1

        print("--------------------------------------")

        for i in range(20, 100):
            print(i)
            if i == 30:
                break

        print("--------------------------------------")

        for x in range(1, 20):
            if x % 2 == 0:
                continue
            else:
                print(x)


class B:
    # public variables (by default)
    b_string_variable = "My name is Keshav Sharma"  # string
    b_number_variable = 123  # numeric (integer)
    b_float_variable = 23.45  #
    b_complex_integer_variable = 234j
    b_complex_float_variable = 244.534j
    b_d = 101
    b_list = [235, 544, 633, 547, 896, "Keshav", "Aman", "Rahul", "Jyoti"]
    b_set = {"Keshav", "Keshav", 283, 213}
    b_set1 = set(["Keshav", "Keshav", 223, 237])
    b_frozenset = frozenset(["Keshav", "Keshav", 923, 723])
    b_tuple = (243, 154, 156, 198, 112, 117, "raghu", "rajeev", "anvar")
    b_dictionary = {"one": 111, "two": 222, 333: "three", 444: "four"}

    # protected variables (can be accessed within class and derived class)
    _b_d = 234  # private variable
    __b_A932432jsgg = "asdfff"

    # private variable (can be accessed only within the class)
    __b_d = 441124  # value cannot be overridden (final value)
    __b_var1, __b_var2, __b_var3 = "asdafaffaawa", 32434, 2323j

    def operators_basics(self):
        a = 33
        b = 7
        print(a + b)  # 40
        print(a - b)  # 26
        print(a / b)  # 4.714285714285714
        print(a % b)  # 5
        print(a // b)  # 4
        print(a * b)  # 231
        print(a ** b)  # 42618442977
        print(a > b)  # True
        print(a < b)  # False
        print(a >= b)  # True
        print(a <= b)  # False
        print(a == b)  # False
        print(a != b)  # True
        c = "cat"
        d = "dog"
        print(c > d)  # ascii values comparison # False
        print(ord("a"))  # printing ascii value of c
        print(ord("v"))
        print('apple' > 'apple')  # False
        print('apple' >= 'apple')  # True
        print('apple' < 'apple')  # False
        print('apple' <= 'apple')  # True
        print(60 > 50 > 40 > 30 > 20 > 10)  # True
        print(1 == True)  # True
        print(0 == False)  # True
        print(10 == 10.0)  # True
        print("way_2_auto" == "way_2_auto")  # True

        print(12 and 23)  # 23
        print(True and False)  # False
        print(False and True)  # False
        print(True and True)  # True
        print(False and False)  # True
        print(43 and 13)  # 13

        print(12 or 23)  # 12
        print(True or False)  # True
        print(False or True)  # True
        print(True or True)  # True
        print(False or False)  # False
        print(43 or 13)  # 13

        print(not True)  # false
        print(not False)  # true
        print(not 20)  # false
        print(not 0)  # true
        print(not 1)  # false

        e = 30
        f = 20
        e += f
        print(e)  # 50
        print(f)  # 20

        e = 30
        e += 1
        print(e)  # 31

        e = 30
        e *= 10
        print(e)  # 300

        e = 30
        e -= 10
        print(e)  # 20

        e = 30
        e /= 10
        print(e)  # 3.0

        e = 36
        e %= 10
        print(e)  # 6

        e = 54
        e //= 23
        print(e)  # 2

        f = 35
        g = 71
        h = 35
        print(35 if f > g else 71)  # 71
        print(35 if f == h else 71)  # 35

        i = 72
        j = 39
        k = 72
        l = k
        print(i is k)  # True
        print(i is not k)  # False
        print(i is l)  # True
        print(i is not l)  # False

        b_list = [23, 54, 23, 34, 35, 76, 98, 9, 23, "keshav", "f", 575, 37, 347, 47]
        print(23 in b_list)  # true
        print("keshav" not in b_list)  # false

    def comprehension(self):
        b1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, "one", "two", "three", "four", "five"]
        b1_1 = [x for x in b1 if type(x) is str]
        b1_2 = [x for x in b1 if x == 9]
        b1_3 = [x for x in b1 if type(x) is int and x % 2 == 0 or type(x) is str]
        print(b1_3)

        b2 = {1, 2, 3, 4, 5, 6, 7, 8, 5, 3, 4, 6, 78, 4, 3, 2, 3, 4, 5, 6, 76, 5}
        b2_1 = {x for x in b2 if x % 2 == 0}
        print(b2_1)
        print(type(b2_1))

        b3 = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
              9: "nine"}
        b3_1 = {x: b3.get(x) for x in b3.keys() if x % 2 == 0}
        print(b3_1)

    def list_basics(self):
        b_list = ["a", 'b', '''c''', """d""", 34, 56, 2, 7, 9, 10, 34 + 5j, True, False, 345.65, 6.78]
        b_1_list = [23, 544, 12, 10, 89, 90, 73456, 58, 123, 522349, 78, 640, 925, 10]
        b_2_list = [234, 534, 122, 1078, 650, 972, 150]
        print(b_list)
        print(type(b_list))
        print(b_list[1])
        print(b_list[3])
        print(b_list[8])
        b_list.append("Kinder Garden")
        print(b_list)
        print(b_list.index("""d""", 3))
        print(b_list.count(7))
        b_1_list.sort()
        print(b_1_list)
        b_1_list.sort(reverse=True)
        print(b_1_list)

        b2_list = ["sharma", "keshu", 34, 56]
        b3_list = ["turmoil", "kronch", 52, 33]
        b2_list = b2_list * 2  # repetition
        print(b2_list)
        b4_list = b2_list + b3_list
        print(b4_list)
        print("sharma" in b2_list)
        print("keshu" not in b2_list)
        for n in b3_list:
            print(n)
        print(" ".join([str(n) for n in b3_list]))
        print(len(b2_list))
        print(max(b_1_list))
        print(max(b_1_list, b_2_list))
        print(min(b_1_list))
        b_4_list = "Keshav Sharma"
        print(list(b_4_list))
        b_5_list = b_2_list[:]
        print(b_5_list)
        print(b_2_list)
        del b_5_list

        b_6_list = [0, 1, 2, 3, 4, 5]
        b_7_list = [6, 7, 8, 9, 10]
        b_8_list = ["zero", "one", "two", "three", "four", "five"]
        b_10_list = [0, 1, 2, 3, 4, 5, 4, 6, 2, 7, 8, 9, 4, 6, 8, 9, 7, 0, 2, 5, 1, 7, 3, 6, 5, 2, 8, 5]
        b_10_list = [0, 1, 2, 3, 4, 5, 4, 6, 2, 7, 8, 9, 4, 6]

        del b_10_list[4]
        print("sasffsfsf : ", b_10_list)

        # joining 2 or more list elements via zip function as tuples
        b_9_list = list(zip(b_8_list, b_6_list, b_7_list))
        print(b_9_list)
        print(type(b_9_list))
        print(type(b_9_list[0]))

        # dictionary in which key is digit and there count is value
        print({n: b_10_list.count(n) for n in b_10_list})

        # remove all elements from list which is duplicate
        b_11_list = [n for n in b_10_list if b_10_list.count(n) != 1]
        print([x for x in b_10_list if x not in b_11_list])

        # remove all elements from list which are duplicate except 1 occurrence
        print(list(set(b_10_list)))
        print(" ".join("keshav".split() * 5))


obj_b = B()
obj_b.list_basics()


class C:
    c1 = "seeOne"
    _c2 = "seeTwo"
    __c3 = "seeThree"

    def __init__(self, c4, c5):
        self.c4 = c4
        self.c5 = c5
        print(f"This is c class constructor {self.c4}")
        print(f"This is c class constructor {self.c5}")
        print(f"This is c class constructor {self.c1}")
        print(f"This is c class constructor {self._c2}")
        print(f"This is c class constructor {self.__c3}")
        print("This is c class constructor")

    def addition(self, a, b):
        print(a + b, "c class addition")

    def c_subtraction(self):
        print("c class subtraction")


class D:
    d1 = "deeOne"
    _d2 = "deeTwo"
    __d3 = "deeThree"

    def __init__(self):
        print("This is d class constructor")

    def addition(self, a, b):
        print(a + b, "d class addition")

    def d_subtraction(self):
        print("d class subtraction")


class E(C, D):
    e1 = "ieeOne"
    _e2 = "ieeTwo"
    __e3 = "ieeThree"

    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2
        C.__init__(self, self.e1, self.e2)
        D.__init__(self)
        print("This is e class constructor")
        print(f"This is e class constructor {self.__e3}")

    def e_subtraction(self):
        print("e class subtraction")


class F:
    f1 = "affOne"
    _f2 = "affTwo"
    __f3 = "affThree"

    def __init__(self):
        print("This is f class constructor")

    def addition(self, a, b):
        print(a + b, "f class addition")

    def f_subtraction(self):
        print("f class subtraction")


print("----------------------------------------------------------------")

obj_c = C("one", "two")
obj_c.addition(1, 1)
obj_c.c_subtraction()

print("----------------------------------------------------------------")

obj_d = D()
obj_d.addition(2, 2)
obj_d.d_subtraction()

print("----------------------------------------------------------------")

obj_e = E("one", "two")
obj_e.addition(3, 3)
obj_e.e_subtraction()
obj_e.d_subtraction()
obj_e.c_subtraction()

print("----------------------------------------------------------------")

obj_f = F()
obj_f.addition(4, 4)
obj_f.f_subtraction()

# variable = lambda arguments : expression
x = lambda a: a * 2
y = lambda a, b: a * b
z = lambda a, b, c: a + b + c
print(x(11), y(11, 11), z(11, 11, 11))


def myfunction(n):
    return lambda a: a * n


# doubler function
mf = myfunction(2)
print(mf(11))

# tripled function
mf = myfunction(3)
print(mf(11))

qwe = [1, 2, 3, 4]
iop = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four"}


def asdf(a, b, *abc, **abcd):
    print(a)
    print(b)
    for item in abc:
        print(item)
    for key, value in abcd.items():
        print(f"{key} = {value}")


asdf(1, 2, 3, 4, 5, 6, 7, 8, 9, first="one", second=10, third=15, fourth=20)

