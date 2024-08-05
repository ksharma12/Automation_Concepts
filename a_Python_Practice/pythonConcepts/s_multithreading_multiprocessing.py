import threading
import time

list_1 = [2, 3, 8, 9]


# at same time
# square_root_list = [4, 9, 64, 81]
# cube_root_list = [8, 27, 512, 729]

def calculate_square(list_1):
    print("calculate square of numbers")
    for n in list_1:
        time.sleep(0.2)
        print('square: ', n ** 2)


def calculate_cube(list_1):
    print("calculate cube of numbers")
    for n in list_1:
        time.sleep(0.2)
        print('cube: ', n ** 3)


# lst = [2, 3, 8, 9]
# t = time.time()
# calculate_square(lst)
# calculate_cube(lst)
#
# print(f"\nDone in: {time.time() - t} seconds")
# print("work complete")

lst = [2, 3, 8, 9]
t = time.time()
t1 = threading.Thread(target=calculate_square, args=(lst,))
t2 = threading.Thread(target=calculate_cube, args=(lst,))

# both the threads started in parallel
t1.start()
t2.start()

#  wait until both the threads executed completely
t1.join()
t2.join()

print(f"Done in: {time.time() - t} seconds")
print("work complete")
