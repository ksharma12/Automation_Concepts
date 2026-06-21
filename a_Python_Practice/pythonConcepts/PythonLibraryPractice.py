class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, n):
        other = 0
        j = 1
        count = 0
        count_prime = 0
        for i in range(0, n + 1):
            while i ** 2 <= j:
                if j % i == 0:
                    other = j // i
                    if i != other:
                        count += 2
                    else:
                        count += 1
                i += 1
                if count == 2:
                    count_prime += 1
                else:
                    pass
            return count_prime
