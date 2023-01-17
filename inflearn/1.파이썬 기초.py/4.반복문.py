# a = range(1, 11)
# print(list(a))

# for i in range(10):
#     print(i)

# for i in range(1, 10):
#     print(i)


# # ## 0까지 가면서 1씩 작아진다.
# # for i in range(10, 0, -1):
#     print(i)

"""
i = 1
while i <= 10:
    print(i)
    i = i + 1

## i 하나씩 작아지는것
# true false개념
i = 10
while i >= 1:
    print(i)
    i = i - 1
"""
## break 보통 무한 반복을 피하는데 쓰인다.
# i = 1
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1
# i = 1
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)

####for else 구문임
## 조건 중간에 break가 생기지 않으면 else로 넘어간다.
for i in range(1, 11):
    print(i)
    if i == 5:
        break
else:
    print(11)
