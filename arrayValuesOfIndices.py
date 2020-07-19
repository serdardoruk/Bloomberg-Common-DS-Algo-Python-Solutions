'''
Input a = [21,5,6,56,88,52], output = [5,5,5,4,-1,-1] . Output array values is made up of indices of the element with value 
greater than the current element but with largest index. So 21 < 56 (index 3), 21 < 88 (index 4) but also 21 < 52 (index 5) 
so we choose index 5 (value 52). Same applies for 5,6 and for 56 its 88 (index 4). If there is no greater element then use -1 
and last element of the array will always have value of -1 in output array since there is no other elment after it. Follow up 
to consider the input as a stream, how can we only update smaller element (use specific Data structure), running time and space 
complexity discussion.

Input a = [21,5,6,56,88,52], output = [5,5,5,4,-1,-1]

'''
from heapq import heappush, heappop
def find_right_index(nums):
    heap = [] 
    for i, val in enumerate(nums):
        heappush(heap, (-val, i))
    print(heap)
    res = [-1]*len(nums)
    maxIdx = -1
    while heap:
        _, curIdx = heappop(heap)
        if curIdx > maxIdx or nums[maxIdx] == nums[curIdx]:
            maxIdx = max(curIdx, maxIdx)
            continue
        res[curIdx] = maxIdx
        maxIdx = max(curIdx, maxIdx)
    return res

print(find_right_index([21,5,6,56,88,52]))

