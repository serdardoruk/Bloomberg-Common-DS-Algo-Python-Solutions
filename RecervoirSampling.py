'''
Given a distinct array of elements. Find n non-repeating random elemnents.

For ex: [2,4,1,-19,56,23,0,34,112,5] , n =3
Output: [ 112,56,23]

Constraints:

Each number has to get equal chance to be in the random set
What is the complexity of the solution?

'''
import random
def reservoir_sampling(nums, n):
    for i in range(len(nums)):
        swap_index = random.randrange(i, len(nums))
        nums[i], nums[swap_index] = nums[swap_index], nums[i]
    return random.sample(nums, n)
print(reservoir_sampling([2,4,1,-19,56,23,0,34,112,5], 3))