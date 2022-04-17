# 2675

T = int(input())

for _ in range(T):
    S, P = input().split()
    for i in P:
        print(i * int(S), end='')
    print()