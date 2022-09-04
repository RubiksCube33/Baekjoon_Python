burger = [1] * 51
patty = [1] * 51
N, X = map(int, input().split())

def GetPatty(N, X):
    if(N == 0) : return 1
    if(X == 1) : return 0

    if(X < burger[N]//2 + 1):
        return GetPatty(N-1, X-1)
    elif(X == (burger[N]//2 + 1)):
        return patty[N-1] + 1;
    else:
        return patty[N-1] + 1 + GetPatty(N-1, X - (burger[N]//2 + 1));

for i in range(1, N+1):
    patty[i] = 2*patty[i-1] + 1;
    burger[i] = 2*burger[i-1] + 3;

print(GetPatty(N, X));