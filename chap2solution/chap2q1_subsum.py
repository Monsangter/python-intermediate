hongildong = {'국어':80, '영어':75, '수학':55}
score = list(hongildong.values()) #list안만들어주면 dict_value반환 주요 함수 실행불가
sum = 0
subnum =len(score) #와일문 실행이후에 len score하면 zero반환됨
while score:
    sum += score.pop()

avg = sum/subnum
print(avg)