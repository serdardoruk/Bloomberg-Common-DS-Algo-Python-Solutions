'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.
'''
            # MIN NUMBER
def findMin(nums):
    if len(nums) == 1:
        return nums[0]
    
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] < nums[mid - 1]:
            return nums[mid]
        elif nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        
        if nums[l] > nums[r]:
            if nums[mid] > nums[l]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid - 1
        
        else:
            return nums[l]

print(findMin([3,4,5,1,2]))


            # TARGET NUMBER

def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        print(nums[mid])
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1