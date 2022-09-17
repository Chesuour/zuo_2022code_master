from typing import List

"""
建立哈希表，记录数据
"""

class Solution:
    def twoSum( nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i,num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []



if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(Solution.twoSum( nums, target))