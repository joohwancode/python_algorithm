"""

반복문을 이용한 문제풀이 
1) 1~N까지 홀수 출력하기 
2) 1부터 N까지의 합 구하기 
3) N의 약수출력하기 


n = int(input())

for i in range(1, n + 1):
    if i % 2 == 1:
        print(i)
"""

# n = int(input())

# sum = 0

# for i in range(1, n + 1):
#     sum = sum + i
# print(sum)

n = int(input())

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")  ###기본적으로 개행이 있는데 개행 없애고 출력한다.
