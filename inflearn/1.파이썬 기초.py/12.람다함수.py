def plus_one(x):
    return x + 1


print(plus_one(1))

plus_two = lambda x: x + 2
print(plus_two(2))

##그럼 왜 람다를 쓰는 것이냐 굳이
##인자에다가 바로 함수를 쓸 수 있음
def plus_one(x):
    return x + 1


a = [2, 3, 4]

print(list(map(plus_one, a)))
print(list(map(lambda x: x + 1, a)))
