"""
Data : 2022/8/16
Author : SuquanChen
Address: 出门问问 苏州

数组为{3, 2, 2, 3, 1}，查询为(0, 3, 2)
意思是在数组里下标0~3这个范围上 有几个2 ?答案返回2。
假设给你一个数组arr,
对这个数组的查询非常频繁，都给出来
请返回所有查询的结果
"""

class Solution():
    def process(arr,left,right,tar):
        subarr = arr[left:right].sort
        mid = Solution.quicksort(arr)
        ans = 0
        for i in range(len(arr)):
            if arr[i] == mid:
                ans +=1
            return mid

    def quicksort(arr):
        mid = len(arr)//2
        l ,r = 0, right-left
        while l < r:
            if arr[mid] > tar :
                return Solution.quicksort(arr[mid+1:])
            elif arr[mid] < tar:
                return Solution.quicksort(arr[:mid-1])
            else:
                return mid
        return -1

        


if __name__=="__main__":
    arr = [3,2,2,3,1]
    left, right = 0, 3
    tar = 2
    print(Solution.process(arr,left,right,tar))
