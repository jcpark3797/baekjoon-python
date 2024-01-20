# 색종이
# 문제번호: 2563번 (4)

# 고민)
# (N,M)에서 좌표 상 각각 +10씩 한 값 전체를 이중 for문을 사용
# 모든 좌표를 탐색하여 0인 값을 1로, 1인 값은 유지하여 넓이를 계산

database = [[0 for _ in range(100)] for _ in range(100)]

num = int(input())
for _ in range(num):
    N, M = map(int, input().split(" "))
    for i in range(N-1, N+9):
        for j in range(M-1, M+9):
            print(i,j)
            if i<100 or j<100:
                database[i][j] = 1
print(sum([database[k].count(1) for k in range(100)]))