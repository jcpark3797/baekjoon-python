# 세로읽기
# 문제번호: 10798번 (3)

DATA = []
max_ = -1
for i in range(5):
    data = input()
    if max_<len(data): max_=len(data)
    DATA.append(data)
    
completeWord = ''
for j in range(max_):
    for i in range(len(DATA)):
        if len(DATA[i]) > j :
            completeWord += DATA[i][j]
print(completeWord)