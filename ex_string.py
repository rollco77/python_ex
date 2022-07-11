# 문자열 표현
a = "Hello Python"
b = """
이 사이에 엔터를 치면서
막 이렇게 치시면 
나중에 print()함수로 출력했을 때
여러줄로 출력됩니다.
"""

a1 = "Su's python"
a2 = 'Su"s python'

print(a)
print(b)

# 문자열 슬라이싱
c = 'hello python'

print(c[0])
print(c[11]) 
print(c[-1]) 
print(c[-2]) 

#formating 
"현재 시간은 오전 %d시입니다" %7
"현재 시간은 %s %d시입니다" %('오전',7)
"현재 시간은 %s %s시입니다" %('오전',7)
