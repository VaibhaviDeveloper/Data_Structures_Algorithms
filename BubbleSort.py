class Solution:
    def bubbleSort(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
    
nums=[7,4,1,5,3]
s=Solution()
s.bubbleSort(nums)
print(nums)