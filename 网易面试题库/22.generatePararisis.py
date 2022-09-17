class Solution():
    def generateParasis(n):
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            if left == 0 and right == 0:
                res.append(cur_str)
                return

            if left > right :
                return

            if left > 0:
                dfs(cur_str+ '(', left - 1, right)

            if right > 0:
                dfs(cur_str + ')', left, right -1)

        dfs(cur_str, n, n)
        return res

if __name__=="__main__":
    n = 4
    print(Solution.generateParasis(n))