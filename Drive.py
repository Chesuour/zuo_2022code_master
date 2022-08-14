"""
Data : 2022/8/12
Author : SuquanChen
Address: 出门问问 苏州

现有司机N*2人 调度中心会将所有司机平分给A、B两个区域
第i个司机去A可得收入为income[i][0],
第i个司机去B可得收入为income[i][1].
返回所有调度方案中能使所有司机总收入最高的方案，是多少钱
"""

class Solution():
    def Driver(income):
        N = len(income)
        if N < 0 or N%2!=0 or not income:
            return 0
        M = N//2
        return Solution.process(income, 0, M)
    def process(income, index, rest):
        N = len(income)
        if index == N:
            return 0
        # 当剩下的名额正好是A剩下的名额，直接调度A剩下的名额，不用考虑B
        if N - index == rest:
            print(1)
            print(income[index][0] + Solution.process(income, index+1, rest-1))
            return income[index][0] + Solution.process(income, index+1, rest-1)
        # 如果A没名额，直接全部调度B
        if rest == 0:
            print(2)
            print(income[index][1] + Solution.process(income, index+1, rest))
            return income[index][1] + Solution.process(income, index+1, rest)

        # 其他情况下，调度比较大小
        p1 = income[index][0] + Solution.process(income, index+1, rest-1)
        p2 = income[index][1] + Solution.process(income, index+1 , rest)

        return max(p1, p2)

    def Driver_dp(income):
        N = len(income)
        M = N//2
        """
        int N = income.length;
		int M = N >> 1;
		int[][] dp = new int[N + 1][M + 1];
		for (int i = N - 1; i >= 0; i--) {
			for (int j = 0; j <= M; j++) {
				if (N - i == j) {
					dp[i][j] = income[i][0] + dp[i + 1][j - 1];
				} else if (j == 0) {
					dp[i][j] = income[i][1] + dp[i + 1][j];
				} else {
					int p1 = income[i][0] + dp[i + 1][j - 1];
					int p2 = income[i][1] + dp[i + 1][j];
					dp[i][j] = Math.max(p1, p2);
				}
			}
		}
		return dp[0][M];
        """
        dp = [[0 for i in range(M+1)]for j in range(N+1)]
        for i in range(N-1,-1,-1):
            # print("i is :", i)
            for j in range(M+1):
                # print("j is :", j)
                if N-i == j:
                    dp[i][j] = income[i][0] + dp[i+1][j-1]
                elif j == 0:
                    dp[i][j] = income[i][1] + dp[i+1][j]
                else:
                    p1 = income[i][0] + dp[i+1][j-1]
                    p2 = income[i][1] + dp[i+1][j] 
                    dp[i][j] = max(p1, p2)
                # print(dp[i][j])
        print(dp)
        return dp[0][M]


                

if __name__=="__main__":
    income = [[9,13], [45,60]]
    print(Solution.Driver(income))
    print(Solution.Driver_dp(income))