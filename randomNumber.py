import time, collections

def randomNumber(start, end):
    timee = time.time() * 1000000
    print(timee)

    num = int(timee) % (end - start + 1) + start

    return num

# print(randomNumber(0,10))

nums = collections.defaultdict(int)
for i in range(10000):
    num = randomNumber(0,20)
    nums[num] += 1

print(nums)