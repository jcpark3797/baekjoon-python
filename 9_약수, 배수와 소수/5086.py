# 배수와 약수
# 문제 번호: 5086번 (1)
'''
    정답 제출 후 소스코드 문제점
    ** 굳이 check, value 크기비교가 없어도 됨!
    ** 수정코드
    while True:
        check, value = map(int,input().split())
        if check == 0 and value == 0: break
        if value%check==0:
            print("factor")
        elif check%value==0:
            print("multiple")
        else:
            print("neither")
            
'''
while True:
    check, value = map(int,input().split())
    if check == 0 and value == 0: break
    if check < value:
        if value%check==0:
            print("factor")
    else:                  
        if check%value==0:
            print("multiple")
            
    if ((check<value)and(value%check!=0))or((check>value)and(check%value!=0)):
        print("neither")
        
        
