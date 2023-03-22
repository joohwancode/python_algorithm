# ## 1번 회문 문자열 검사

# import sys

# sys.stdin = open("input.txt", "rt")

# # # n = int(input())

# # # for i in range(n):
# # #     s = input()
# # #     s = s.upper()
# # #     ##반만 돌면서 비교한다.
# # #     size = len(s)
# # #     for j in range(size // 2):
# # #         if s[j] != s[-1 - j]:
# # #             print("# %d NO" % (i + 1))
# # #             break
# # #     else:
# # #         print("# %d YES" % (i + 1))
# # ##2번째 방법

# # # n = int(input())

# # # for i in range(n):
# # #     s = input()
# # #     s = s.upper()
# # #     if s != s[::-1]:
# # #         print("# %d NO" % (i + 1))
# # #     else:
# # #         print("# %d YES" % (i + 1))


# # ## 2번
# # # s = input()
# # # res = 0
# # # for x in s:
# # #     if x.isdecimal():
# # #         res = res * 10 + int(x)
# # # cnt = 0
# # # ##range를 잘잡자
# # # for i in range(1, res + 1):
# # #     if res % i == 0:

# # #         cnt += 1
# # # print(res, cnt)

# # ##3번

# # # a = list(range(21))
# # # # 계속돌면서 하나씩해준다.
# # # for _ in range(10):
# # #     s, e = map(int, input().split())
# # #     for i in range((e - s + 1) // 2):
# # #         a[s + i], a[e - i] = a[e - i], a[s + i]
# # # a.pop(0)
# # # for x in a:
# # #     print(x, end=" ")


# # ##4번
# # # n = int(input())

# # # a = list(map(int, input().split()))

# # # k = int(input())
# # # b = list(map(int, input().split()))
# # # # 중복된거 빼줄 필요도 없음
# # # ##리스트 더한다
# # # ##for 문으로 숫자로 출력되도록

# # # c = a + b
# # # c.sort()
# # # for x in c:
# # #     print(x, end=" ")

# # # 위처럼 하라는게 아님


# # # n = int(input())
# # # a = list(map(int, input().split()))
# # # k = int(input())
# # # b = list(map(int, input().split()))
# # # c = []
# # # p1 = p2 = 0
# # # while p1 < n and p2 < k:
# # #     if a[p1] < b[p2]:
# # #         c.append(a[p1])
# # #         p1 += 1
# # #     else:
# # #         c.append(b[p2])
# # #         p2 += 1
# # # if p1 < n:
# # #     c = c + a[p1::]
# # # if p2 < k:
# # #     c = c + b[p2::]
# # # for x in c:
# # #     print(x, end=" ")
# # # print(c)

# # n, m = map(int, input().split())
# # a = list(map(int, input().split()))

# # tot = a[0]
# # lt = 0
# # rt = 1
# # cnt = 0
# # while True:
# #     ##3가지 경우로 나눈다.
# #     if tot < m:
# #         # rt가 n보다 작을때까지만 돈다 .
# #         if rt < n:
# #             tot += a[rt]
# #             rt += 1
# #         else:
# #             break
# #     elif tot == m:
# #         cnt += 1
# #         tot -= a[lt]
# #         lt += 1
# #     else:
# #         tot -= a[lt]
# #         lt += 1
# # print(cnt)

# # ##6번
# # n = int(input())
# # arr = [list(map(int, input().split())) for i in range(n)]
# # ##행과 열의 합부터 구한다.
# # largest = -214700000
# # for i in range(n):
# #     sum1=sum2=0

# ##7번 사과나무
# # n = int(input())
# # a = [list(map(int, input().split())) for _ in range(n)]
# # res = 0
# # s = e = n // 2
# # for i in range(n):
# #     for j in range(s, e + 1):
# #         res += a[i][j]
# #     if i < n // 2:
# #         s -= 1
# #         e += 1
# #     else:
# #         s += 1
# #         e -= 1
# # print(res)
# ##8번 모래시계

# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# k = int(input())
# for _ in range(k):
#     h, t, b = map(int, input().split())
#     ##왼쪽 회전
#     for _ in range(k):
#         a[h - 1].append(a[h - 1].pop(0))
#     else:
#         a[h - 1].insert(0, a[h - 1].pop())
# print(a)
# s = 0
# e = n - 1
# res = 0

# for i in range(n):
#     for j in range(s, e + 1):
#         res += a[i][j]
#     if i < n // 2:
#         s += 1
#         e -= 1
#     else:
#         s -= 1
#         e += 1
# ###들여쓰기 계속 틀림 확인하지 if else : i
# print(res)


##9번 봉우리
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]
# a.insert(0, [0] * n)
# a.append([0] * n)
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# cnt = 0
# for x in a:
#     x.insert(0, 0)
#     x.append(0)
#     print(x)
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
#             cnt += 1
# print(cnt)
# 10번 스도쿠 검사


# def check(a):
#     for i in range(9):  # 행, 열 체크
#         ch1 = [0] * 10
#         ch2 = [0] * 10
#         for j in range(9):
#             ch1[a[i][j]] = 1
#             ch2[a[j][i]] = 1
#         if sum(ch1) != 9 or sum(ch2) != 9:
#             return False
#     for i in range(3):  # 그룹 체크, 4중 for문
#         for j in range(3):
#             ch3 = [0] * 10
#             for k in range(3):
#                 for s in range(3):
#                     ch3[a[i * 3 + k][j * 3 + s]] = 1
#             if sum(ch3) != 9:
#                 return False
#     return True


# a = [list(map(int, input().split())) for _ in range(9)]

# if check(a):
#     print("YES")
# else:
#     print("NO")
