import itertools
#
# A = [2, 1, 6, 4]
#
#
# # for i in range(0, len(A)):
# #     print(i)
#
# #
# def index_counter(A):
#     count = 0
#     B = A.copy()
#     all_prefix_sum = list(itertools.accumulate(A))  # This calculate prefix sum
#     for i in range(0, len(B)):
#         ele = B.pop(i)
#         all_sum_except_1 = all_prefix_sum[-1] - ele
#         B[1::2] = [0] * len(B[1::2])
#         even_prefix_sum = list(itertools.accumulate(B))
#         odd_prefix_sum = all_sum_except_1 - even_prefix_sum[-1]
#         if odd_prefix_sum == even_prefix_sum[-1]:
#             count += 1
#         else:
#             pass
#         B = A.copy()
#     print(count)
#
#
# index_counter([1, 1, 1])


# [13, 7, 16, 18, 14, 17, 18, 8, 10]
# [4]
# [4,4,4]
# def solve(A):
#     if 1 < len(A) and len(set(A)) != 1:
#         largest = max(A)
#         A = [x for x in A if x != largest]
#         return max(A)
#     else:
#         return -1


# [1, 2, 3, 7, 1, 2, 3]
# [1,2,5,1,2]
# def solve(A):
#     P = list(itertools.accumulate(A))
#     print(P)
#     for i in range(0, len(P)):
#         if P[i - 1] == (P[-1] - P[i]):
#             return i
#     return -1



