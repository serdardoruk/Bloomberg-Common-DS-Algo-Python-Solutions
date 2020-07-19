'''Given [1,5,12,67,98], create a function prints [2->4, 6->11,13->66, 68->97] '''

array = [1,5,12,67,98]

def pairs(nums):

    for i in range(len(nums) - 1):
        print(nums[i] + 1, " --> ", nums[i + 1] - 1)


pairs(array)