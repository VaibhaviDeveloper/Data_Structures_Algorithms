def InsetionSort(nums):
    n=len(nums)
    for i in range(n):
        j=i-1
        key=nums[i]
        while(j>=0 and nums[j]>key):
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key

nums=[5,3,7,3,2,9]
InsetionSort(nums)
print(nums)