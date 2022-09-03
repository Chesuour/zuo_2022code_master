"""
Data : 2022/9/3
Author : SuquanChen
Address: yangzhou unversity
~~
leetcode原题
这里有一个非负整数数组 arr，你最开始位于该数组的起始下标 start 处。当你位于下标 i 处时，你可以跳到 i + arr[i] 或者 i - arr[i]。
请你判断自己是否能够跳到对应元素值为 0 的 任一 下标处。
注意，不管是什么情况下，你都无法跳到数组之外。

示例 1：
输入：arr = [4,2,3,0,3,1,2], start = 5
输出：true
解释：
到达值为 0 的下标 3 有以下可能方案： 
下标 5 -> 下标 4 -> 下标 1 -> 下标 3 
下标 5 -> 下标 6 -> 下标 4 -> 下标 1 -> 下标 3 
示例 2：

输入：arr = [4,2,3,0,3,1,2], start = 0
输出：true 
解释：
到达值为 0 的下标 3 有以下可能方案： 
下标 0 -> 下标 4 -> 下标 1 -> 下标 3
示例 3：

输入：arr = [3,0,2,1,2], start = 2
输出：false
解释：无法到达值为 0 的下标 1 处。
"""

class Solution:
    def CanJump(arr, start):
        """
        使用setset保存每个位置是否已经遍历过
        使用递归
        递归终止条件： 当前下标超范围 则直接返回False
        如果当前位置是0 则直接返回True
        若当前位置已经遍历过 直接返回False
        最后 Recursion(i - arr[i])Recursion(i−arr[i]) or Recursion(i + arr[i])Recursion(i+arr[i])
        """
        memo = set()
        def Recursion(i):
            if i < 0 or i >= len(arr):
                return False
            if arr[i] == 0:
                return True
            if i in memo:
                return False
            memo.add(i)
            return Recursion(i - arr[i]) or Recursion(i + arr[i])
        return Recursion(start)

if __name__=="__main__":
    arr, start = [4,2,3,0,3,1,2], 0
    print(Solution.CanJump(arr, start))