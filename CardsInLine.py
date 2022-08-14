"""
Data : 2022/8/5
Author : SuquanChen
Address: 出门问问 苏州

Some busy happens 

给定一个整型数组arr 代表数值不同的纸牌排成一条线
玩家A和玩家B依次拿走每张纸牌
规定玩家A先拿 玩家B后拿
但是每个玩家每次只能拿走最左或最右的纸牌
玩家A和玩家B都绝顶聪明
请返回最后获胜者的分数。
"""


from re import A


class Solution_cur():
    def beforehand(arr, L, R):
        if L==R:
            return arr[L]
        p1 = arr[L] + Solution_cur.afterhand(arr, L+1, R)
        p2 = arr[R] + Solution_cur.afterhand(arr, L, R-1)
        return max(p1,p2)

    def afterhand(arr, L, R):
        if L == R:
            return 0
        p1 = Solution_cur.beforehand(arr, L+1, R)
        p2 = Solution_cur.beforehand(arr, L, R-1)
        return min(p1,p2)

    def CardsInLine(arr):
        if not arr and len(arr) == 0:
            return 0
        before = Solution_cur.beforehand(arr, 0, len(arr)-1)
        after  = Solution_cur.afterhand(arr, 0, len(arr)-1)
        return max(before, after)

class Solution_dp():
    def beforehand(arr, L, R, before_dp, after_dp):
        if before_dp[L][R] != -1:
            return before_dp[L][R]
        ans = 0
        if L==R:
            return arr[L]
        else:
            p1 = arr[L] + Solution_dp.afterhand(arr, L+1, R, before_dp, after_dp)
            p2 = arr[R] + Solution_dp.afterhand(arr, L, R-1, before_dp, after_dp)
            ans = max(p1,p2)
        before_dp[L][R] = ans
        return ans

    def afterhand(arr, L, R, before_dp, after_dp):
        if after_dp[L][R] != -1:
            return after_dp[L][R]
        ans = 0
        if L != R:
            p1 = Solution_dp.beforehand(arr, L+1, R, before_dp, after_dp)
            p2 = Solution_dp.beforehand(arr, L, R-1, before_dp, after_dp)
            ans = min(p1,p2)
        after_dp[L][R] = ans 
        return ans

    def CardsInLine_dp(arr):
        if not arr or len(arr) == 0:
            return 0
        N = len(arr)
        before_dp = [[-1 for i in range(N)]for j in range(N)]
        after_dp  = [[-1 for i in range(N)]for j in range(N)]
        before = Solution_dp.beforehand(arr, 0, len(arr)-1, before_dp, after_dp)
        after  = Solution_dp.afterhand(arr, 0, len(arr)-1, before_dp, after_dp)
        return max(before, after)

class Solution_second_dp():
    def CardsInLine_dp2(arr):
        if  arr == None or len(arr) == 0:
                return 0
        N = len(arr)
        fmap, gmap = [[0 for i in range(N)]for j in range(N)],[[0 for i in range(N)]for j in range(N)]
        # for i in range(N):
        #     fmap[i][i] = arr[i]
        # for startCol in range(N):
        #     L, R =0, startCol
        #     while R < N:
        #         fmap[L][R] = max(arr[L] + gmap[L + 1][R], arr[R] + gmap[L][R - 1])
        #         gmap[L][R] = min(fmap[L + 1][R], fmap[L][R - 1])
        #         L +=1
        #         R +=1
        for j in range(0, N):
            fmap[j][j] = arr[j]
            for i in range(j-1, 0,-1):
                fmap[i][j] = max(arr[i]+ gmap[i+1][j],arr[j] + gmap[i][j-1])
                gmap[i][j] = min(fmap[i+1][j], fmap[i][j-1])
        return max(fmap[0][N - 1], gmap[0][N - 1])




if __name__=="__main__":
    print(Solution_cur.CardsInLine([5, 7, 4, 5, 8, 1, 6, 0, 3, 4, 6, 1, 7 ]))

    print(Solution_dp.CardsInLine_dp([5, 7, 4, 5, 8, 1, 6, 0, 3, 4, 6, 1, 7 ]))

    print(Solution_second_dp.CardsInLine_dp2([5, 7, 4, 5, 8, 1, 6, 0, 3, 4, 6, 1, 7 ]))