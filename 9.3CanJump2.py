"""
Data : 2022/9/3
Author : SuquanChen
Address: yangzhou university

leetcode原题
给你一个非负整数数组 arr ，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。


示例 1:
输入: arr = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

示例 2:
输入: arr = [2,3,0,1,4]
输出: 2
"""

class Solution():
    def CanJump(arr):
        if not arr or len(arr)==0:
            return 0
        step, cur, next= 0, 0, 0
        # step 跳的步数，cur表示在上一个位置最多能在走到的位置，next就是最大走的范围的那个值，下一次到达的位置
        for i in range(len(arr)):
            if cur < i:
                step +=1
                cur = next
            next = max(next, i+arr[i])
        return step

            
if __name__=="__main__":
    arr = [3,4,1,3,2,4,2,1,2,4,2,3,2]
    print(Solution.CanJump(arr))