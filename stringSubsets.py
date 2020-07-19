'''
Given a string print all subsets (not permutations)
Eg. String "abc" should output

empty string
a
b
c
ab
bc
ac
abc
'''
#   SOLUTION ONE
# def subsets(string):
#     nums = list(string)
#     subs = [[]]

#     for num in nums:
#         subs += [[num] + sub for sub in subs]
    
#     for sub in subs:
#         print("".join(sub))
    
#   SOLUTION TWO
def subsets(string):

    def backtrack(first, cur):
        if len(cur) == k:
            print("".join(cur))

        for i in range(first, len(string)):
            cur.append(string[i])
            backtrack(i + 1, cur)
            cur.pop()
            
    for k in range(len(string) + 1):
        backtrack(0, [])
    
    
subsets("abc")