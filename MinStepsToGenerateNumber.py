'''
https://leetcode.com/discuss/interview-question/406663/Bloomberg-or-Phone-Screen-or-Min-Steps-to-Generate-Number

Given an int n. You can use only 2 operations:

multiply by 2
integer division by 3 (e.g. 10 / 3 = 3)
Find the minimum number of steps required to generate n from 1.

Example 1:

Input: 10
Output: 6
Explanation: 1 * 2 * 2 * 2 * 2 / 3 * 2
6 steps required, as we have used 5 multiplications by 2, and one division by 3.
Example 2:

Input: 3
Output: 7
Explanation: 1 * 2 * 2 * 2 * 2 * 2 / 3 / 3
7 steps required, as we have used 5 multiplications by 2 and 2 divisions by 3.

'''
from collections import deque
def minNumber(n):
    q=deque([(1,0)])
    seen=set()

    while q:
        res,ops = q.popleft()

        if res==n:
            return ops

        if res*2 not in seen:
            q.append((res*2,ops+1))
            seen.add(res*2)

        if res//3 and res // 3 not in seen:
            q.append((res//3,ops+1))
            seen.add(res//3)


print(minNumber(10)) 
print(minNumber(3)) 
print(minNumber(11))