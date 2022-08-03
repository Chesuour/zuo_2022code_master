"""
Data : 2022/8/3
Author : SuquanChen
Address: 出门问问 苏州

输入：
一根绳子的长度 l
一个数组，数组中包含了一堆坐标点

输出：
用绳子覆盖坐标点，最多能覆盖的点数
"""


class Solution():
    def __init__(self) -> None:
        pass
    
    def CoverMaxPoint(arr, tar):
        left, right, length, res = 0, 0, len(arr), 0
        while left< length:
            while right < length and (arr[right]-arr[left] <= tar):
                right +=1
            
            res = max(res, right - left)
            left +=1
        return res

if __name__=="__main__":
    arr = [1,3,4,5,6,8,9,12,14,16,18,22,23,24,25,26,27,30,100,101,102,103,104,105,106,107,108]
    tar = 9
    res = Solution.CoverMaxPoint(arr,tar)
    print(res)



