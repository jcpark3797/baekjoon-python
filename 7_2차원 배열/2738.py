# 행렬 덧셈
# 문제번호: 2738번 (1)

# 두  행렬 A, B 저장할 변수
A, B = [], []

# N*M 행렬에 대한 입력
N, M = map(int, input().split(" "))

# N열에 관한 입력 (각 A, B)
for i in range(N):
    A.append(list(map(int, input().split(" "))))
for i in range(N):
    B.append(list(map(int, input().split(" "))))

# A행렬 + B행렬 => 출력
for n in range(N):
    T = []
    for m in range(M):
        T.append(str(A[n][m] + B[n][m]))
    print(" ".join(T))