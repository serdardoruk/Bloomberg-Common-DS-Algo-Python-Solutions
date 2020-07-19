'''
Remove ints from an array.

Example:

Input: array = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76], ranges = [[5, 8], [10, 13], [3, 6], [20, 25]]
Output: [-8, 3, -5, 29, 43, 76, 73, 76]
Is there a corresponding or relative leetcode question?

'''
array = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76]
ranges = [[5, 8], [10, 13], [3, 6], [20, 25]]

def removeRanges(array, ranges):
    for rang in ranges:
        for i in range(rang[0], rang[1]):
            if i <= len(array):
                array[i] =  "D"
    
    left = 0
    while array[left] != "D":
        left += 1

    for right in range(left + 1, len(array)):
        if array[right] != "D":
            array[left] = array[right]
            left += 1
    
    print(array[:left])
removeRanges(array, ranges)