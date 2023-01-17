## 함수가 왜 존재하는지
##무조건 main 스크립트 위에 있어야 한다.
# def add(a, b):
#     c = a + b
#     return c


# x = add(2, 3)
# print(x)
# print(add(2, 3))


###함수 튜플형태로도 가능하다 .
# def add(a, b):
#     c = a + b
#     d = a - b
#     return c, d


# print(add(2, 3))

##소수구하는 함수 만들기
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


a = [12, 19, 13, 17, 33, 23]

for y in a:
    if isPrime(y):
        print(y, end=" ")
