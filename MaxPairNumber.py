"""
Data : 2022/8/15
Author : SuquanChen
Address: 出门问问 苏州

能同时比赛的最大场次
"""

class Solution():
    def MaxPairNumber(arr,k):
        if not arr and k < 0 and len(arr) < 2:
            return 0 
        arr.sort()
        left, right = 0, 1
        ans = 0
        N = len(arr)
        used = [0 for i in range(N)] 
        while left < N and right < N:
            if used[left] == -1:
                left += 1
            elif left >= right:
                right +=1
            else :
                distance = arr[right] - arr[left]
                if distance == k :
                    left += 1
                    right +=1
                    ans +=1
                    used[right] = -1
                elif distance < k:
                    right += 1
                else :
                    left += 1
        return ans
            

if __name__ == "__main__":
    arr = [1,1,3,3,5,7]
    k = 2
    print(Solution.MaxPairNumber(arr,k))