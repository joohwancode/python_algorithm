a = [23, 43, 57, 89, 100]


# for i in range(len(a)):
#     print(a[i], end=" ")
# print()
# for x in a:
#     print(x, end=" ")
# print()
# for x in a:
#     if x % 2 == 1:
#         print(x, end=" ")
# print()
# for x in enumerate(a):
#     print(x, end=" ")
# b = (1, 2, 3, 4, 5, 6, 7)
# print()
# print(b[0])
# print(b)
# ### 튜플은 변경이 불가하다 .

# ##밑에 2개가 같은것이다.
# for x in enumerate(a):
#     print(x[0], x[1])

for index, value in enumerate(a):
    print(index, value)
if all(0 < x for x in a):
    print("YES")
else:
    print("NO")
if any(30 < x for x in a):
    print("YES")
else:
    print("NO")
###any는 하나라도 맞으면 true 임
