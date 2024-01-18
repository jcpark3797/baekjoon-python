# 너의 평점은
# 조건: 전공평점 3.3이상 or 졸업고사 통과
    # 전공평점 = 전공과목별 (학점 x 과목평점)의 합을 학점 총합으로 나눈 값
    
total = []
score_total = 0
grade_dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
       'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

# 20과목을 입력하기 위한 반복문
for i in range(20): 
    name, score, grade = input().split(" ")
    if grade != 'P':
        total.append(float(score) * grade_dic[grade])
        score_total += float(score)
print(sum(total)/score_total)