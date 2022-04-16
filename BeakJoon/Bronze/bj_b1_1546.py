# 1546

N = int(input())
score_list = list(map(int,input().split()))

print(sum(score_list)/max(score_list)*100/N)