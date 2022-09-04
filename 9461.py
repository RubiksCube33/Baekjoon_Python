arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

repeat = int(input())

answer = 0
for j in range(0,repeat):
  num = int(input())
  if num < (len(arr)):
    answer = arr[num]
  else:
    for i in range(len(arr),num+1):
        temp = arr[i-1] + arr[i-5]
        arr.append(temp)
    answer = arr[len(arr)-1]
  print(answer)