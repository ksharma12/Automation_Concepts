import numpy as np

# CATEGORIES OF NUMPY FUNCTION

# 1.Array Creation and Manipulation:

# np.array(): Creates an array from a Python list or tuple.
np_x_homo_list = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
np_x1_tupple = np.array((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
np_x2_hetro_list = np.array([1, "ramu", True, 5.34])  # convert all to string type

print(np_x2_hetro_list)
print(type(np_x2_hetro_list))
print(len(np_x2_hetro_list))
print(np_x2_hetro_list[0])
print(np_x2_hetro_list.dtype)  # to check ele type of numpy array

print("--------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------")

# np.zeros(), np.ones(), np.full(): Creates arrays filled with zeros, ones, or a specified constant value.

# np.zeros()
np_z = np.zeros(10)  # gives array of 10 zeros
print(np_z)  # gives float values
print(np_z.astype(int))  # to convert whole array eles type to another

print("--------------------------------------------------------------------------------------------------")

# np.ones()
np_one = np.ones(10)
print(np_one)  # gives float values
print(np_one.astype(int))

print("--------------------------------------------------------------------------------------------------")

# np.full()
np_full_1 = np.full(5, 10)  # 1D array of size 5 with values 10
print(np_full_1)
print("--------------------------------------------------------------------------------------------------")
np_full_2 = np.full((3, 4), 10)  # (3X4)D array with values 10
print(np_full_2)
print("--------------------------------------------------------------------------------------------------")
np_full_3 = np.full((3, 4), "X")  # (3X4)D array with Symbol "X"
print(np_full_3)
print("--------------------------------------------------------------------------------------------------")
np_full_4 = np.full((3, 4), 4.6, dtype=float)  # (3X4)D array with value 4.6 and datatype float
print(np_full_4)

print("--------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------")

# np.arange(): Creates an array with evenly spaced values within a given interval.
np_r_1 = np.arange(5)
print(np_r_1)
print("--------------------------------------------------------------------------------------------------")
np_r_2 = np.arange(2, 30)
print(np_r_2)
print("--------------------------------------------------------------------------------------------------")
np_r_3 = np.arange(30, 3, -1)
print(np_r_3)
print("--------------------------------------------------------------------------------------------------")
np_r_4 = np.arange(30, 3, -4)
print(np_r_4)
print("--------------------------------------------------------------------------------------------------")
np_r_5 = np.arange(0.9, 3.0, 0.3)
print(np_r_5)
print("--------------------------------------------------------------------------------------------------")
np_r_6 = np.arange(5.9, 2.7, -0.4)
print(np_r_6)

print("--------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------")

# np.reshape(): Changes the shape of an array without changing its data.
np_s_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])  # 1D array
np_s_1_reshape = np_s_1.reshape(4, 2)  # reshape linear array to 2D 5 X 2 array
print(np_s_1_reshape)
print("--------------------------------------------------------------------------------------------------")
np_s_2_reshape = np_s_1.reshape(2, 2, 2)  # reshape linear array to 3D 2 X 2 X 2 array
print(np_s_2_reshape)
print("--------------------------------------------------------------------------------------------------")
np_s_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])  # 2D Array
np_s_3_reshape = np_s_1.reshape(3, 4)  # reshape linear array to 3D 2 X 2 X 2 array
print(np_s_3_reshape)
print("--------------------------------------------------------------------------------------------------")
np_s_4_reshape = np_s_1.reshape(3, 2, 2)  # reshape linear array to 3D 3 X 2 X 2 array
print(np_s_4_reshape)
print("--------------------------------------------------------------------------------------------------")
np_s_5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # 1D array
# Reshape to 2 rows, letting NumPy determine the number of columns
np_s_5_reshape = np_s_5.reshape(3, -1)  # reshape linear array to 2D array 2 X [anonymour] array
print(np_s_5_reshape)
print("--------------------------------------------------------------------------------------------------")
# Reshape to 3 colums, letting NumPy determine the number of rows
np_s_6_reshape = np_s_5.reshape(-1, 3)  # reshape linear array to 2D array 2 X [anonymour] array
print(np_s_6_reshape)

print("--------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------")

np_t_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])  # 2D Array 4 x 3
print(np_t_1.transpose())  # [4x3 array converts to 3x4 array]
print("--------------------------------------------------------------------------------------------------")
np_t_2 = np.array(np.array([[[1, 2],
                             [3, 4]],
                            [[5, 6],
                             [7, 8]]]))  # 3D Array 2 x 2 x 2
# original axis = 0,1,2
# after transpose = 1,0,2
print(np_t_2)
print("-------------------------")
print(np_t_2.transpose(0, 1, 2))
print("-------------------------")
print(np_t_2.transpose(0, 2, 1))
print("-------------------------")
print(np_t_2.transpose(1, 0, 2))
print("-------------------------")
print(np_t_2.transpose(1, 2, 0))
print("-------------------------")
print(np_t_2.transpose(2, 0, 1))
print("-------------------------")
print(np_t_2.transpose(2, 1, 0))

print("--------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------")

# np.concatenate(), np.vstack(), np.hstack(): Joins arrays.

np_array_1 = np.array([1, 2, 3, 4, 5])
np_array_2 = np.array([6, 7, 8, 9, 10])
print(np.concatenate((np_array_1, np_array_1)))

print("--------------------------------------------------------------------------------------------------")

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(np.concatenate((arr1, arr2), axis=0)) # concatinate along rows
print("--------------------------------------------------------------------------------------------------")
print(np.concatenate((arr1, arr2), axis=1)) # concatinate along colums
print("--------------------------------------------------------------------------------------------------")
print(np.concatenate((arr1, arr2), axis=None)) # concatinate and flatten

print("--------------------------------------------------------------------------------------------------")

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([5, 6])
print(np.concatenate((arr1, arr2), axis=None))  # flatten the arrays
