class Solution(object):
    def nextPermutation( nums):
        n =len(nums)
        i, k = n-2,n-1
        while i >= 0 and nums[i] >= nums[i+1]:
            i -=1
        if i >= 0:
            while k >= 0 and nums[i] >= nums[k] :
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]

        nums[i+1 : n] =  reversed(nums[i+1:n])

        return nums



if __name__ == "__main__":
    nums = [3,2,1]
    nums1 = [1,2,3,8,5,7,6,4]
    print(Solution.nextPermutation(nums1))