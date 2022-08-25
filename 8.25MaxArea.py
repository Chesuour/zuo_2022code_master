"""
Data : 2022/8/25
Author : SuquanChen
Address: 出门问问 苏州


leetcode原题 

给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。
"""

class Solution():
    def maxArea(height) -> int:
        left, right = 0, len(height)-1
        res = 0
        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
        return res



if __name__=="__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution.maxArea(height))
