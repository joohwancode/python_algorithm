# a = input("숫자를 입력하세요:")
# print(a)

###문자형으로 나온다 .
"""a, b = input("숫자를 입력하세요: ").split()
print(a + b)"""

a, b = map(int, input("숫자를 입력하세요: ").split())

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  ##몫
print(a % b)  ## 나머지
print(a**b)  ###a를 b번 거듭제곱
