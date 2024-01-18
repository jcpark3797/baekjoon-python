# 최댓값
# 문제번호: 2566번 (2)

# 문제는 이차원 행렬을 저장하여 최댓값과 위치를 찾는 것이긴 하다.
# 하지만 꼭 그렇게 해결하진 않아도 될 것 같아서 아래와 같이 해결함!

# 한번 틀렸는데 maxindex 기본값 설정이 0이 아닌 -1로 설정해야 한다.
# 조건 중에 자연수 또는 0이라는 조건 때문에 틀린 것 같다 ㅠ

maxindex = [-1,'']
for n in range(9):
    data = list(map(int, input().split(" ")))
    if max(data) > maxindex[0]:
        maxindex[0] = max(data)
        maxindex[1] = str(n+1) + ' ' + str(data.index(max(data))+1)

print(maxindex[0])
print(maxindex[1])