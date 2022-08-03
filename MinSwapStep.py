"""
Data : 2022/8/3
Author : SuquanChen
Address: 出门问问 苏州

// 一个数组中只有两种字符'G'和'B'
	// 可以让所有的G都放在左侧,所有的B都放在右侧
    // 或者可以让所有的G都放在右侧,所有的B都放在左侧
	// 但是只能在相邻字符之间进行交换操作，请问请问至少需要交换几次，
"""

class Solution():
    def MinSwapStep(arr):
        if not arr: return 0
        l= 0
        step1, step2 = 0, 0
        for i in range(len(arr)):
            if arr[i] == 'G':
                step1 += (i - l)
                l +=1
        for j in range(len(arr)):
            if arr[i] == 'B':
                step2 += (j-l)
                l +=1
        return max(step1, step2) 

if __name__ == "__main__":
    arr = ['G','B','G','G','G','B','G','B','B'] 
    res = Solution.MinSwapStep(arr)
    print("the result is :", res)       