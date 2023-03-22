# import sys
# from collections import deque

# sys.stdin = open("input.txt", "rt")


# ###2번 쇠막대기와 레이저###################################################################################################
# # s = input()
# # stack = []
# # cnt = 0

# # for i in range(len(s)):
# #     if s[i] == "(":
# #         stack.append(s[i])
# #     else:
# #         ##이전이 '('인지 확인한다.
# #         if s[i - 1] == "(":
# #             stack.pop()
# #             cnt += len(stack)
# #         else:
# #             stack.pop()
# #             cnt += 1
# # print(cnt)

####3번 후위 표기식 만들기###################################################################################################
# a = input()
# stack = []
# res = ""
# for x in a:
#     if x.isdecimal():
#         res += x
#     else:
#         if x == "(":
#             stack.append(x)
#         elif x == "*" or x == "/":
#             while stack and (stack[-1] == "*" or stack[-1] == "/"):
#                 res += stack.pop()
#             stack.append(x)
#         elif x == "+" or x == "-":
#             while stack and stack[-1] != "(":
#                 res += stack.pop()
#             stack.append(x)
#         elif x == ")":
#             while stack and stack[-1] != "(":
#                 res += stack.pop()
#             stack.pop()  ##마지막 지운다\\
# while stack:
#     res += stack.pop()  ##마지막 남은것도 제거한다.
# print(res)
# a = input()
# stack = []
# for x in a:
#     if x.isdecimal():
#         stack.append(int(x))  ###int화 시켜야 한다.
#     else:
#         if x == "+":
#             n1 = stack.pop()
#             n2 = stack.pop()
#             stack.append(n2 + n1)
#         elif x == "-":
#             n1 = stack.pop()
#             n2 = stack.pop()
#             stack.append(n2 - n1)  ## 나중에 나온게 빼기를 당하는 것이다.
#         elif x == "*":
#             n1 = stack.pop()
#             n2 = stack.pop()
#             stack.append(n2 * n1)
#         elif x == "/":
#             n1 = stack.pop()
#             n2 = stack.pop()
#             stack.append(n2 / n1)
# print(stack[0])


####4번 공주###################################################################################################
# n, k = map(int, input().split())
# dq = list(range(1, n + 1))
# dq = deque(dq)
# while dq:
#     for _ in range(k - 1):
#         cur = dq.popleft()
#         dq.append(cur)
#     dq.popleft()
#     if len(dq) == 1:
#         print(dq[0])
#         dq.popleft()  ##들여쓰기 잘하기
####5번 응급실###################################################################################################
# n, m = map(int, input().split())
# Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
# Q = deque(Q)
# cnt = 0

# while True:
#     cur = Q.popleft()
#     if any(cur[1] < x[1] for x in Q):#어떤 거라도 큰게 있다면
#         Q.append(cur)
#     else:  ##아무도 큰게없다면
#         cnt += 1
#         if cur[0] == m:
#             print(cnt)
#             break
####6번 교육과정 설계###################################################################################################

# a = list(input())
# n = int(input())
# b = [list(input()) for i in range(n)]
# b = deque(b)
# while b:
#     for k in a:
#         for i in b:
#             for j in i:
#                 if k != j:
#                     i.popleft()
# print(i)
# 위에는 틀린것
# need = input()
# n = int(input())
# for i in range(n):
#     plan = input()
#     dq = deque(need)
#     for x in plan:
#         if x in dq:  ## x가 dq 에 있냐 없냐 확인해야 한다.
#             if x != dq.popleft():
#                 print("#%d NO" % (i + 1))
#                 break
#     else:  ##순서는 통과
#         if len(dq) == 0: ## dq에 없어야 한다. 남은 것이 없어야 함
#             print("#%d YES" % (i + 1))
#         else: ## 있으면 NO
#             print("#%d NO" % (i + 1))
####7번 단어 찾기###################################################################################################
# n = int(input())
# note = []
# dq = deque(note)
# for i in range(n):
#     a = list(input())
#     note.append(a)
# poet = []
# for j in range(n, 9):
#     b = list(input())
#     poet.append(b)
# for x in poet:
#     for x in dq:
#         if x == dq:
#             dq.popleft()
#             print(dq)
###위에는 오답
##딕셔너리로 접근해야 하는데 그러지 못했음
# n = int(input())
# p = dict()
# for i in range(n):
#     word = input()
#     p[word] = 1
# for i in range(n - 1):
#     word = input()
#     p[word] = 0
# for key, val in p.items():
#     if val == 1:
#         print(key)
####8번 아나 그램####################################################################################################
# a = input()
# b = input()
# str1 = dict()
# str2 = dict()
# for x in a:
#     str1[x] = str1.get(x, 0) + 1
# print(str1)
# for x in b:
#     str2[x] = str2.get(x, 0) + 1
# print(str2)
# for i in str1.keys():
#     if i in str2.keys(): #str1에 있는 키값들이 str2에도 있어야 한다.
#         if str1[i] !=str2[i]:## value가 같아야 한다.
#             print("NO")
#             break
#     else:
#         print("NO")
#         break
# else:
#     print("YES")
####8번 아나 그램 개선 방법 ####################################################################################################

# a = input()
# b = input()
# sH = dict()
# for x in a:
#     sH[x] = sH.get(x, 0) + 1
# for x in b:
#     sH[x] = sH.get(x, 0) - 1
# for x in a:
#     if sH.get(x) > 0:
#         print("NO")
#         break
# else:
#     print("YES")
####9.1번 아나그램 리스트 해쉬 ###################################################################################################
# a = input()
# b = input()
# ##알파벳 소문자 26 대문자 26 총 52개 필요
# str1 = [0] * 52
# str2 = [0] * 52
# for x in a:
#     if x.isupper():
#         str1[ord(x) - 65] += 1 ## 아스키 코드 대문자 A는 65번임
#     else:
#         str1[ord(x) - 71] += 1 ##아스키 코드 소문자 a는 97번인데 대문자가 끝난 26번째 부터 시작해야 하므로 71을 뺀다.
# for x in b:
#     if x.isupper():
#         str2[ord(x) - 65] += 1
#     else:
#         str2[ord(x) - 71] += 1
# for i in range(52):
#     if str1[i] != str2[i]:
#         print("NO")
#         break
# else:
#     print("YES")
####10번최소힙  ###################################################################################################
# import sys
# import heapq as hq

# sys.stdin = open("input.txt", "rt")
# # ##힙자료구조 처럼 움직임
# a = []
# while True:
#     n = int(input())
#     if n == -1:
#         break
#     if n == 0:
#         if len(a) == 0:
#             print(-1)
#         else:
#             print(hq.heappop(a))
#     else:
#         hq.heappush(a, n)
####11번 최대힙  ###################################################################################################
# a = []
# while True:
#     n = int(input())
#     if n == -1:
#         break
#     if n == 0:
#         if len(a) == 0:
#             print(-1)
#         else:
#             print(-hq.heappop(a))  ###pop할때 -로 하기
#     else:
#         hq.heappush(a, -n)
