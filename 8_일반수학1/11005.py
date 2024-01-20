# 진법 변환2
# 문제 번호: 11005번 (2)

import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base):
    k, v = divmod(num, base) # 몫, 나머지 구하기
    if k == 0:
        return tmp[v]
    else:
        return convert(k, base) + tmp[v]
NUM, T = map(int, input().split(" "))
print(convert(NUM, T).upper())