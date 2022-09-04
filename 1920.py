import sys

N = int(input())
Nums = list(map(int, sys.stdin.readline().split()))
M = int(input())
Mums = list(map(int, sys.stdin.readline().split()))
Nums.sort()


def binary_search(answer):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        if Nums[mid] == answer:
            return True
        elif Nums[mid] < answer:
            start = mid + 1
        else:
            end = mid - 1
    return False


for i in range(0, M):
    if (binary_search(Mums[i]) == True):
        print("1")
    else:
        print(0)