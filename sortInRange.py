
def partSort(arr, N, a, b): 
    l = min(a, b) 
    r = max(a, b) 

    temp = [0 for i in range(r - l + 1)] 
    j = 0
    for i in range(l, r + 1, 1): 
        temp[j] = arr[i] 
        j += 1

    temp.sort(reverse = False) 
  

    j = 0
    for i in range(l, r + 1, 1): 
            arr[i] = temp[j] 
            j += 1
    for i in range(0, N, 1): 
            print(arr[i], end = " ") 

if __name__ == '__main__': 
    arr = [7, 8, 4, 5, 2] 
    a = 1
    b = 4

    N = len(arr)  
  
    partSort(arr, N, a, b) 
  