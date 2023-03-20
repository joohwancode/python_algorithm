# import sys

# sys.stdin = open("input.txt", "rt")
# ###1번 이분 검색
# # # n, m = map(int, input().split())

# # # a = list(map(int, input().split()))

# # # a.sort()
# # # lt = 0
# # # rt = n - 1

# # # # while 문으로 계속 탐색 while 문 안에 조건이 참일때까지만 돈다 .
# # # while lt <= rt:
# # #     mid = (lt + rt) // 2
# # #     if a[mid] == m:
# # #         print(mid + 1)
# # #         break
# # #     elif a[mid] > m:
# # #         rt = mid - 1
# # #     else:
# # #         lt = mid + 1
# # ##2번(랜선자르기 결정 알고리즘)

# # # k, n = map(int, input().split())
# # # Line = []
# # # largest = 0


# # # def Count(len):
# # #     cnt = 0
# # #     for x in Line:
# # #         cnt += x // len
# # #     return cnt


# # # for i in range(k):
# # #     temp = int(input())
# # #     Line.append(temp)
# # #     largest = max(largest, temp)
# # # lt = 1
# # # rt = largest

# # # while lt <= rt:
# # #     mid = (lt + rt) // 2

# # #     if Count(mid) >= n:
# # #         res = mid
# # #         lt = mid + 1
# # #     else:
# # #         rt = mid - 1
# # # print(res)
# # ##3번 뮤직비디오
# # # def Count(capacity):
# # #     cnt = 1
# # #     sum = 0
# # #     for x in music:
# # #         if sum + x > capacity:
# # #             cnt += 1
# # #             sum = x
# # #         else:
# # #             sum += x
# # #     return cnt


# # # n, m = map(int, input().split())
# # # music = list(map(int, input().split()))
# # # maxx = max(music)

# # # lt = 1
# # # rt = sum(music)
# # # res = 0


# # # while lt <= rt:
# # #     mid = (lt + rt) // 2
# # #     if mid >= maxx and Count(mid) <= m:
# # #         res = mid
# # #         ##정확도를 높여야ㅕ 한다.
# # #         rt = mid - 1
# # #     else:
# # #         lt = mid + 1
# # # print(res)


# ##4번 마구간


# # def Count(len):
# #     cnt = 1
# #     ep = Line[0]
# #     for i in range(1, n):
# #         if Line[i] - ep >= len:
# #             cnt += 1
# #             ep = Line[i]
# #     return cnt


# # n, c = map(int, input().split())
# # Line = []
# # res = 0
# # for _ in range(n):
# #     tmp = int(input())
# #     Line.append(tmp)
# # Line.sort()
# # lt = 1
# # rt = Line[n - 1]
# # while lt <= rt:
# #     mid = (lt + rt) // 2
# #     if Count(mid) >= c:
# #         res = mid
# #         lt = mid + 1
# #     else:
# #         rt = mid - 1
# # print(res)
# ###-----------그리디 ---------#####

# ##1번
# # n = int(input())

# # meeting = []
# # for i in range(n):
# #     s, e = map(int, input().split())
# #     meeting.append((s, e))
# # print(meeting)
# # meeting.sort(key=lambda x: (x[1], x[0]))
# # print(meeting)
# # cnt = 0
# # et = 0
# # for s, e in meeting:
# #     if s >= et:
# #         cnt += 1
# #         et = e

# # print(cnt)
# 2번몸무게만 비교한다.
# n = int(input())
# member = []

# for i in range(n):
#     h, w = map(int, input().split())
#     member.append((h, w))
# member.sort(reverse=True)
# print(member)
# cnt = 0
# largest = 0
# for h, w in member:
#     if w > largest:
#         largest =
#         cnt += 1

# # print(cnt)
# # 몸무게만 비교한다.
# ##3번 창고정리
# # n = int(input())
# # height = list(map(int, input().split()))
# # b = int(input())
# # height.sort()
# # for _ in range(b):
# #     height[0] += 1
# #     height[n - 1] -= 1
# #     height.sort()
# # print(height[n - 1] - height[0])

# ##4번 타이타닉
# # n, limit = map(int, input().split())

# # from collections import deque

# # p = list(map(int, input().split()))
# # p.sort()
# # p = deque(p)

# # ##p라는 리스트가 deque 로 바꾼다.
# # cnt = 0
# # while p:  ##비어있으면 멈춘다.
# #     if len(p) == 1:
# #         cnt += 1
# #     ##한사람이 탄 경우
# #     if p[0] + p[-1] > limit:
# #         p.pop()
# #         cnt += 1
# #     ##2사람이 간 경우
# #     else:
# #         ##그다음 승객을 체크해야 한다.
# #         p.popleft()
# #         p.pop()
# #         cnt += 1
# # print(cnt)

# # 증가수열 만들기 (그리디)## 다시봐야함
# from collections import deque

# n = int(input())
# a = list(map(int, input().split()))
# # 비교할 것이 필요하다.
# last = 0
# lt = 0
# rt = n - 1
# res = ""
# tmp = []
# for i in range(n):
#     if a[lt] > last:
#         tmp.append((a[lt], "L"))
#     if a[rt] > last:
#         tmp.append((a[rt], "R"))
#     tmp.sort()
#     if len(tmp) == 0:
#         break
#     else:
#         res = res + tmp[0][1]
#         last = tmp[0][0]
#         if tmp[0][1] == "L":
#             lt += 1
#         else:
#             rt -= 1
#     tmp.clear()

# print(len(res))
# print(res)
# n = int(input())
# a = list(map(int, input().split()))
# seq = [0] * n
# for i in range(n):
#     for j in range(n):
#         if a[i] == 0 and seq[j] == 0:
#             seq[j] = i + 1
#             break
#         elif seq[j] == 0:
#             a[i] -= 1
# for x in seq:
#     print(x, end=" ")
