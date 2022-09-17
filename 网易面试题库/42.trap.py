from typing import List

class Solution:
    def trap( height: List[int]) -> int:
        ans = 0
        stack = list()
        n = len(height)

        for i,h in enumerate(height):
            while stack and h > height[stack[-1]]:
                # print("#######")
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                
                # print(left)
                cur_Width = i - left -1
                cur_height = min(height[left], height[i]) - height[top]
                ans += cur_Width * cur_height
            stack.append(i)

            # print(stack)
        
        return ans

    def trap_dp( height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)  # 简化的连续赋值
        # 正向遍历数组 height 得到数组 leftMax 的每个元素值
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        # 反向遍历数组 height 得到数组 rightMax 的每个元素值
        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):  # 逆序遍历
            rightMax[i] = max(rightMax[i + 1], height[i])
        # 遍历每个下标位置即可得到能接的雨水总量
        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2 ,1]
            # 0,1,2,3,4,5,6,7,8,9,10,11
    print(Solution.trap(height))
    print(Solution.trap_dp(height))