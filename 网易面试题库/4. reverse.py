class Solution:
    def reverse( x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        res = 0
        while x :
            if res < INT_MIN // 10 + 1 or res > INT_MAX // 10:
                return 0
            a = x %10
            print(a)
            res = res *10 +a
            x = x//10
            # print(x)
        return res


if __name__=="__main__":
    x = 123
    print(Solution.reverse(x))