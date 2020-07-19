'''
Given an array of integers which is initially increasing and then decreasing, find the maximum value in the array.
Examples :

Input: arr[] = {8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1}
Output: 500

Input: arr[] = {1, 3, 50, 10, 9, 7, 6}
Output: 50

Corner case (No decreasing part)
Input: arr[] = {10, 20, 30, 40, 50}
Output: 50

Corner case (No increasing part)
Input: arr[] = {120, 100, 80, 20, 0}
Output: 120

'''
def findMaximum(arr, low, high): 
	if low == high: 
		return arr[low] 

	if high == low + 1 and arr[low] >= arr[high]: 
		return arr[low]; 

	if high == low + 1 and arr[low] < arr[high]: 
		return arr[high] 

	mid = (low + high)//2 

	if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]: 
		return arr[mid] 

	if arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1]: 
		return findMaximum(arr, low, mid-1) 
	else:
		return findMaximum(arr, mid + 1, high) 


arr = [1, 3, 50, 10, 9, 7, 6] 
n = len(arr) 
print ("The maximum element is %d"% findMaximum(arr, 0, n-1)) 


