class Solution:
    # @param A : integer
    # @return an integer

    # TC - O(rootN) , SC - O(1)
    @staticmethod
    def Count_Factors(A):
        other = 0
        i = 1
        count = 0
        while i ** 2 <= A:
            if A % i == 0:
                other = A // i
                if i != other:
                    count += 2
                else:
                    count += 1
            i += 1
        return count

    # TC - O(RootN) , SC - O(RootN)
    @staticmethod
    def Return_Factors(A):
        other = 0
        i = 1
        count = 0
        factors = []
        while i ** 2 <= A:
            if A % i == 0:
                other = A // i
                if i != other:
                    factors.append(other)
                    factors.append(i)
                else:
                    factors.append(i)
            i += 1
        return factors

    # TC - O(RootN) , SC - O(RootN)
    @staticmethod
    def Perfect_Number(A):
        asdf = Solution.Return_Factors(A)
        factors = asdf.sort()
        Number = asdf[-1]
        Sum_All_Except_Number = sum(asdf) - Number
        if Number == Sum_All_Except_Number:
            return 1
        else:
            return 0

    # TC - O(RootN) , SC - O(1)
    @staticmethod
    def Number_Prime_Not(A):
        other = 0
        i = 1
        count = 0
        while i ** 2 <= A:
            if A % i == 0:
                other = A // i
                if i != other:
                    count += 2
                else:
                    count += 1
            i += 1
        if count == 2:
            return 1
        else:
            return 0

    # TC - O(RootN) , SC - O(1)
    @staticmethod
    def Print_Prime_Not(A):
        other = 0
        i = 1
        count = 0
        while i ** 2 <= A:
            if A % i == 0:
                other = A // i
                if i != other:
                    count += 2
                else:
                    count += 1
            i += 1
        if count == 2:
            return "Is Prime"
        else:
            return "Is Not Prime"

    # TC - O(RootN X N) , SC - O(1)
    @staticmethod
    def Count_Prime_Numbers(N):
        count_prime = 0
        for i in range(0, N + 1):
            if Solution.Number_Prime_Not(i) == 1:
                count_prime += 1
        return count_prime

    @staticmethod
    def Count_Prime_Numbers_1(N):
        other = 0
        i = 1
        count = 0
        count_prime = 0
        for A in range(2, N + 1):
            while i ** 2 <= A:
                if A % i == 0:
                    other = A // i
                    if i != other:
                        count += 2
                    else:
                        count += 1
                i += 1
            if count == 2:
                print(A)
        return None


a = Solution()
print(a.Perfect_Number(8))
print(1 + 4 + 9 + 16 + 25)