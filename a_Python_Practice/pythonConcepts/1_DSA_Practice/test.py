class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers

    def reverse(self, A, left, right):
        l = left
        r = right
        while l < r:
            A[l], A[r] = A[r], A[l]  # swaping
            l += 1
            r -= 1

    def solve(self, A, B):
        N = len(A)
        B %= N
        Solution.reverse(self, A, 0, N - 1)  # rotate entire array
        Solution.reverse(self, A, 0, B - 1)  # rotate first k elements
        Solution.reverse(self, A, B, N - 1)  # rotate remaining N-k elements
        print(A)


