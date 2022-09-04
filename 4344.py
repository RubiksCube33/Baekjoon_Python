import sys
n = int(sys.stdin.readline())

for _ in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    scoresum = 0
    for i in range(1,len(nums)):
        scoresum += nums[i]
    avg = scoresum/nums[0]
    answer = 0
    for j in range(1,len(nums)):
        if nums[j] > avg:
            answer += 1
    ratio = (answer/nums[0]) *100
    ratio = str(f'{ratio:.3f}')
    print(ratio+"%")