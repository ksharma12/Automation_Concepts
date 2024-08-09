_variable = 10
__variable = 12  # cannot be overridden


class A:
    a, aa, aaa = 10, 12j, "aaa"
    _a_protected_variable = "a_protected variable"  # accessed with in the class and derived class
    __a_private_variable = "a_private variable"  # accessed with in the class only
    a_public_variable = "a_public variable"  # accessed freely
    a_integer = 10
    a_float = 10.234
    a_complex = 10j
    a_string = "a_string"
    a_boolean = True
    a_exponent = 2 ** 10  # 2^10
    a_list = [10, "a", "aaa", 12.345, 23j]  # list
    a_tuple = (10, "a", "aaa", 12.345, 23j)  # tuple
    a_set = {10, "a", "aaa", 12.345, 23j}  # set
    a_frozenset = frozenset((10, "a", "aaa", 12.345, 23j))
    a_dictionary = {"a1": 1, "a2": 2, "a3": 3, "a4": 4, "a5": 5}
    aa_string = "This house belongs to Keshav Sharma"
    aaa_string = "  This is Keshav Sharma   "

    def printing_some_values(self):
        print(f"100/100 is {100 / 100}")
        print(f"100//100 is {100 // 100}")
        print(f"11 % 3 is {11 % 3}")
        a_typecast1 = "qwerty"
        a_typecast2 = 0
        a_typecast3 = 123
        print(f"qwerty to boolean is {bool(a_typecast1)}")
        print(f"0 to boolean is {bool(a_typecast2)}")
        print(f"1234 to boolean is {bool(a_typecast3)}")
        print(f"a_typecast2 variable is instance of integer: {isinstance(a_typecast2, int)}")
        print(f"a_typecast2 variable is instance of integer: {isinstance(a_typecast1, str)}")

    def String_methods(self):
        # Slicing The String
        print(A.aa_string[4])
        print(A.aa_string[5])
        print(A.aa_string[0:10])
        print(A.aa_string[0:10:1])
        print(A.aa_string[0:10:3])
        print(A.aa_string[::-1])
        print(len(A.aaa_string))
        print(A.aaa_string.strip())
        print(A.aaa_string.lower())
        print(A.aaa_string.upper())
        a_concatinate_1 = "the"
        a_concatinate_2 = "is"
        print(a_concatinate_1 + a_concatinate_2)
        print("The" * 8)  # this string repeat itself 8 times
        print("a" + "b" * 2)  # BOADMASS rule
        # string formatters
        city = "Gurugram"
        age = 31
        id = 7.23
        print("hey i live in", city)
        print(f"Hey i live in {city} and my age is {age} and my id is {id}")
        print("Hey i live in {} and my age is {} and my id is {}".format(city, age, id))
        print("Hey i live in %s and my age is %d and my id is %f" % (city, age, id))

    def Questions(self):
        # reverse the words but same order
        a_reverse_same_order = "editor and run it"
        a_reverse_same_order_1 = list(a_reverse_same_order.split())
        print(" ".join([n[::-1] for n in a_reverse_same_order_1]))

        # reverse order and reverse word in the string
        a_string_a = "Sun rises in the east far away mountains"
        print(a_string_a[::-1])
        # same order but reverse word in a string
        print(" ".join([n[::-1] for n in a_string_a.split()]))

        # Same words but reverse order in the string
        print(" ".join(a_string_a.split()[::-1]))

    def loops(self):
        a_list_a = ["asdf", "qwer", "tyui", "lkjh", "mnbv", "dfgh"]
        for aa in a_list_a:
            print(aa)
        print("----------------------------------------------------------")
        for x in range(1, 5):
            print(x)
        print("----------------------------------------------------------")
        for x in range(1, 10, 3):
            print(x)
        print("----------------------------------------------------------")
        sequence = "KeshavSharma"
        for x in sequence:
            print(f"The charracter {x} index is {sequence.index(x)}")
        print("----------------------------------------------------------")
        i = 0
        while i < 10:
            print(i)
            i += 1
        print("------------------list comprehention_-------------------------")
        a_comp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        a_comp_1 = [n for n in a_comp if n % 2 == 0]
        print(a_comp_1)  # list of even numbers
        print(type(a_comp_1))
        print("------------------set comprehention_-------------------------")
        a_set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        a_set_2 = {n for n in a_comp if n % 2 == 0}
        print(a_set_2)  # set of even numbers
        print(type(a_set_2))
        print("------------------dictionary comprehention_-------------------------")
        a_dict_1 = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        a_dict_2 = {n: n for n in a_dict_1.values() if n % 2 == 0}
        print(a_dict_2)

    def list(self):
        x = []
        a_l = [1, 2, 3, 'asdf', "Keshav", "Keshav", True, 34.65, 3 + 4j]
        print(type(a_l))
        print(a_l[4])
        a_l.append("corry anderson")
        print(a_l)
        a_list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(a_list_1[5:])
        del a_list_1[9]
        print(a_list_1)
        print(a_list_1[:5])
        print(a_list_1[:])
        print(a_list_1[::])
        print(a_list_1[::-1])
        print(a_list_1[5:0:-1])
        print(a_list_1[5:0:-2])
        print(a_list_1[0::2])
        # repetition of same items
        alist_2 = [1, 2, 3, True, "Keshav", 3 + 5j]
        alist_4 = [9, 8, 7, False, "Sharma", 7 - 3j]
        alist_3 = alist_2 * 2
        alist_5 = alist_4 + alist_2
        print(alist_3)
        print(alist_5)
        print("Keshav" in alist_2)
        print("Keshav" not in alist_2)

    def tuple(self):
        a_tuple = (1, 2, 3, 4, 5, "Keshav", 34.23, True)
        print(a_tuple[3])
        print(a_tuple[:3])

        original_tuple = (1, 2, 3, 4)
        new_tuple_1 = tuple(original_tuple)
        print(new_tuple_1)

    def dictionary(self):
        a_d1 = {
            1: "24dsdsf",
            "F.Name": "Keshav",
            "L.Name": "Sharma",
            "Age": 31
        }
        a_d2 = {
            "F.Name": "Keshav",
            "L.Name": "Sharma",
            "Age": 31,
            "IsMarried": False,
            "Salary": 1000000000.10
        }
        print(a_d1[1])
        print(f"First Name : {a_d2['F.Name']}")
        print("__------------------------------------------------------------")
        for x in a_d2:
            print(x)
        print("__------------------------------------------------------------")
        for x in a_d2:
            print(a_d2[x])
        print("__------------------------------------------------------------")
        for a in a_d2.values():
            print(a)
        print("__------------------------------------------------------------")
        for a in a_d2.items():
            print(a)
        print("__------------------------------------------------------------")
        for a in a_d2.keys():
            print(a)
        print("__------------------------------------------------------------")
        items = {
            "fruits": ["Apples", "Banana", "Grapes", "Mango"],
            "Price": {"a": 1213, "b": 2345},
            "Size": 12.8
        }
        print(items["fruits"][2])
        print(items.get("Price").get("b"))
        print(items["Price"]["b"])
        print(len(items))
        print("--------------------------------------------------------------------------------------")
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 6, 6, 6, 4, 3, 3, 3, 4]
        print(len(lst))
        print({n: lst.count(n) for n in lst})


class B(A):
    _b_protected_variable = "b_protected variable"
    __b_private_variable = "b_private variable"
    b_public_variable = "b_public variable"


a = A()
a.dictionary()
