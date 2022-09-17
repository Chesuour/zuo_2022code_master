class Solution:
    def minDistance(word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)

        if m*n == 0: return m+n

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i

        for j in range(n+1):
            dp[0][j] = j

        # print(dp)

        for i in range(1, m+1):
            for j in range(1, n+1):
                left = dp[i-1][j] +1
                down = dp[i][j-1] +1
                left_down = dp[i-1][j-1]
                #如果最后一个字符不一样，那么就要在做一步，如果一样就可以省去一步
                if word1[i-1] != word2[j-1]:
                    left_down +=1
                dp[i][j] = min(left, down, left_down)

        # print(dp)
        return dp[m][n]

if __name__=="__main__":
    word1 = "horse"
    word2 = "ros"

    word3 = "intention"
    word4 = "execution"
    print(Solution.minDistance(word1, word2))
    print(Solution.minDistance(word3, word4))
