"""
Data : 2022/8/16
Author : SuquanChen
Address: 出门问问 苏州


给定一个正数数组arr代表若干人的体重
再给定一个正数limit表示所有船共同拥有的载重量
每艘船最多坐两人，且不能超过载重
想让所有的人同时过河，并且用最好的分配方法让船尽量少
返回最少的船数

自己写的代码，和视频不一样，我觉得也不错
"""

class Solution():
    def BoatsToSavePeople(arr, limit):
        arr.sort()
        if not arr or arr[-1]>limit:
            return 0
        left, right, boats = 0, len(arr)-1, 0
        weight = [0 for i in range(len(arr))]
        index = 0
        while left < right:
            index +=1
            if index >10:
                break
            if weight[right] != -1 :
                if arr[left] + arr[right] <= limit :
                    weight[right] = -1
                    weight[left] = -1
                    left +=1
                    right -=1
                    boats +=1
                else :
                    right -=1
            print(f"left:{left},right:{right},boats:{boats}")
            print(weight)
            
        for i in range(len(weight)):
            if weight[i] != -1:
                boats +=1
        return boats


if __name__=="__main__":
    arr = [1,7,4,5,2,3,6,9,3,5,8,8,6,4,3,7,9]
    limit =10
    print(Solution.BoatsToSavePeople(arr, limit))