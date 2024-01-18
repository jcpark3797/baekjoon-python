# 색종이
# 문제번호: 2563번 (4)

database = [[0]*100]*100

num = int(input())
for n in range(num):
    i,j = map(int, input().split(" "))
    end_i, end_j = i+10, j+10
    