'''
Number of ways to divide n objects in k groups, such that no group will have fewer objects than previously formed groups?

2


Example: n=8, k=4 Answer: 5

[1,1,1,5], [1,1,2,4], [1,1,3,3], [1,2,2,3], [2,2,2,2]

I thought of applying dynamic programming to count the number of ways 8 objects can be divided into 4 groups, 
but can't understand how to keep track of the number of objects in the previous group.
'''

# function f(n, k, memo={}){
#   if (k == 0 && n == 0)
#     return 1

#   if (n <= 0 || k <= 0)
#     return 0

#   let key = String([n, k]) // Thanks to comment by user633183

#   if (memo.hasOwnProperty(key))
#     return memo[key]

#   return memo[key] = f(n - k, k, memo) + f(n - 1, k - 1, memo)
# }

# console.time('time taken')
# console.log(f(1000, 10))
# console.timeEnd('time taken')

def f(n, k, memo = {}):
    if k == 0 and n == 0:
        return 1

    if n <= 0 or k <= 0:
        return 0

    key = str((n, k))

    if key in memo:
        return memo[key]

    memo[key] = f(n - k, k, memo) + f(n - 1, k - 1, memo)
    return memo[key]

print(f(8, 4))

