"""
Data : 2022/8/3
Author : SuquanChen
Address: 出门问问 苏州

leetcode 494题

给定一个数组arr 可以在每个数字前加 + - ，但是所有数字都要包含
目标值是target  请问最后算出target的方法数是多少
"""

class Solution():
    def TargetSum(arr, tar):
        def process(arr, index, res):
            if index == len(arr): #没有剩余的数字
                #如果剩余的数恰好为0，那么可以处理0，但是，不是0，无法处理
                if res == 0: return 1
                else : return 0
            return process(arr, index+1, res - arr[index]) + process(arr, index+1, res + arr[index])
        return process(arr,0,tar)

         

if __name__ == "__main__":
      arr = [1,3,2,4,6,5,7,8,9,2]
      target = 47
      print(Solution.TargetSum(arr,target))
