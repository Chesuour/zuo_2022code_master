"""
Data : 2022/8/14
Author : SuquanChen
Address: 出门问问 苏州

矩阵的最小路径和
《程序员算法面试指南》题目
"""

class Solution():
    def MatrixMinPath(matrix):
        M = len(matrix)
        N = len(matrix[0])
        if not matrix or M ==0 or N==0 : return 0
        return Solution.process(matrix, 0, 0)

    def process(matrix, row, clo):
        if row == len(matrix)-1 and clo == len(matrix[0])-1:
            # print(1)
            return matrix[row][clo]

        if row == len(matrix)-1 and clo != len(matrix[0])-1:
            # print(2)
            return matrix[row][clo] + Solution.process(matrix,row,clo+1)

        elif clo == len(matrix[0])-1 and row != len(matrix)-1 :
            # print(3)
            return matrix[row][clo] + Solution.process(matrix,row+1,clo)
        else :
            # print(4)
            p1 =matrix[row][clo] + Solution.process(matrix, row+1, clo)
            p2 =matrix[row][clo] +  Solution.process(matrix, row, clo+1)
            return matrix[row][clo] + min(p1, p2)

    def MatrixMinPath_dp(matrix):
        M = len(matrix)
        N = len(matrix[0])
        # print(M,N)
        if not matrix or M ==0 or N==0 : return 0
        dp = [[[0]for i in range(N+1)]for j in range(M+1)]
        dp[0][0] = matrix[0][0]
        for j in range(1,N):
            dp[0][j] = matrix[0][j] + dp[0][j-1]
        for i in range(1,M):
            dp[i][0] =matrix[i][0] + dp[i-1][0]
        for i in range(1,M):
            for j in range(1,N):
                # print(i,j)
                dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[M-1][N-1]
                




if __name__=="__main__":
    """
    1 3 5 9
    8 1 3 4
    5 0 6 1
    8 8 4 0
    """
    matrix =[[1,3,5,9], [8,1,3,4], [5,0,6,1], [8,8,4,0]]
    matrix1 = [[3,1,0,2],[4,3,2,1],[5,2,1,0]] 
    print(Solution.MatrixMinPath(matrix1))
    print(Solution.MatrixMinPath_dp(matrix1))