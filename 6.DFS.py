# import sys

# # import itertools as it

# sys.stdin = open("input.txt", "rt")

############ 1번 stack으로 이루어진 재귀함수 #############
# def DFS(x):
#     if x > 0:
#         DFS(x - 1)
#         print(x, end=" ")


# ##문법이 안되거나 논리가 안됨
# ##문법이 안되는것같음

# if __name__ == "__main__":
#     n = int(input())
# DFS(n)
############ 2번 stack으로 이루어진 재귀함수 #############


# def DFS(x):
#     if x == 0:
#         return
#     else:
#         DFS(x // 2)
#         print(x % 2, end=" ")


# if __name__ == "__main__":
#     n = int(input())
#     DFS(n)
############ 3번 이진트리 순회 #############
# 부왼오-전위순회
# 왼부오-중위순회
# 왼오부-후위순회
# def DFS(x):
#     if x > 7:
#         return
#     else:
#         print(x, end=" ")
#         DFS(2 * x)
#         DFS(2 * x + 1)


# if __name__ == "__main__":
#     DFS(1)

# num, m = map(int, input().split())
# num을 리스트로 만든다.
# num = list(map(int, str(num)))  # str로 바꾸어야 한개씩 접근이 가능하다
# stack = []
# for x in num:
#     while stack and m > 0 and stack[-1] < x:
#         stack.pop()
#         m -= 1
#     stack.append(x)
# if m != 0:
#     stack = stack[:-m]
# res = "".join(map((str, stack)))
# print(res)


# s = input()
# stack = []
# cnt = 0
# for i in len(s):
#     if s[i] == "(":
#         stack.append(s[i])
#     else:
#         if s[i - 1] == "(":  ##여느괄호인지 확인해라
#             stack.pop()
#             cnt += len(stack)
#         else:
#             stack.pop()
#             cnt += 1
# print(cnt)
############ 3번 부분집합 구하기  ############
# def DFS(v):
#     if v == n + 1:
#         for i in range(1, n + 1):
#             if ch[i] == 1: //방문한 곳이라면
#                 print(i, end=" ")
#         print()
#     else:
#         ch[v] = 1
#         DFS(v + 1)
#         ch[v] = 0
#         DFS(v + 1)


# if __name__ == "__main__":
#     n = int(input())
#     ch = [0] * (n + 1)
#     DFS(1)

############ 4번 합이 같은 부분집합  ############
# sum ==total -sum
# L을 깊이와 인덱스로 사용한다.
def DFS(L, sum):
    if L == n:  # 0번 인덱스 부터니까
        if sum == (total-sum):
            print("YES")
            sys.exit(0)  # 프로그램을 아예종료시킨다.
    else:
        DFS(L+1, sum+a[L])  # o
        DFS(L+1, sum)  # x


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")
#
############ 5번 바둑이 승차 ############
# def DFS(L, sum, tsum):  ####tsum -> 판단을 한 무게
#     global result
#     if sum + (total - tsum) < c:  ##total-tsum-> 앞으로 판단을 해야할
#         return
#     if sum > c:
#         return
#     if L == n:
#         if sum > result:
#             result = sum
#     else:
#         DFS(L + 1, sum + a[L], tsum)
#         DFS(L + 1, sum)


# if __name__ == "__main__":
#     c, n = map(int, input().split())
#     a = [0] * n
#     result = -2147000000
#     for i in range(n):
#         a[i] = int(input())
#     total = sum(a)
#     DFS(0, 0, 0)
############# 6번 중복순열 구하기  ############


# def DFS(L):
#     global cnt
#     if L == m:
#         for j in range(m):
#             print(res[j], end=" ")
#         print()
#         cnt += 1

#     ###print 한다.
#     else:
#         for i in range(1, n + 1):
#             res[L] = i
#             DFS(L + 1)


# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     res = [0] * n
#     cnt = 0
#     DFS(0)
#     print(cnt)


############# 7번 동전 구하기  ############


# def DFS(L, sum):
#     global res
#     if L>res:
#         return

#     if sum > m:
#         return
#     if sum == m:
#         if L < res:
#             res = L  ##작은게 발견 되면  res =L을 넣는다 .
#     else:
#         for i in range(n):
#             DFS(L + 1, sum + a[i])


# if __name__ == "__main__":
#     n = int(input())
#     a = list(map(int, input().split()))
#     m = int(input())
#     a.sort(reverse=True)
#     res = 2147000000
#     DFS(0, 0)
#     print(res)
############# 8번 순열  구하기  ############
# def DFS(L):
#     global cnt
#     if L == m:
#         for j in range(m):
#             print(res[j], end=" ")
#         print()
#         cnt += 1
#     else:
#         for i in range(1, n + 1):
#             if ch[i] == 0:
#                 ch[i] = 1
#                 res[L] = i
#                 DFS(L + 1)
#                 ch[i] = 0


# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     ch = [0] * (n + 1)
#     res = [0] * m
#     cnt = 0
#     DFS(0)
#     print(cnt)
############# 9번 순열 추측하기   ############


# def DFS(L, sum):
#     if L == n and sum == f:
#         for x in p:
#             print(x, end=" ")
#         sys.exit(0) ## 여러가지 나와서 발견되면 바로
#     else:  ##곱해주는 것 해야 함
#         for i in range(1, n + 1):
#             if ch[i] == 0:
#                 ch[i] = 1  ##쓰이지 않았다면
#                 p[L] = i
#                 DFS(L + 1, sum + (p[L] * b[L]))
#                 ch[i] = 0


# if __name__ == "__main__":
#     n, f = map(int, input().split())
#     p = [0] * n
#     b = [1] * n  ## 이항 계수 초기화 한다.
#     ch = [0] * (n + 1)  ##왜     N+1 : 1,2,3,4 이기 때문에 0부터 체크해주는 것이 아니다.
#     for i in range(1, n):
#         b[i] = b[i - 1] * (n - i) // i
#     DFS(0, 0)

############# 10번 조합   ############
# def DFS(L, s):
#     global cnt
#     if L == m:
#         for i in range(L):
#             print(res[i], end=" ")
#         cnt += 1
#         print()
#     else:
#         for j in range(s, n + 1):
#             res[L] = j
#             DFS(L + 1, j+1)


# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     res = [0] * (n + 1)
#     cnt = 0
#     DFS(0, 1)  ##s는 1부터 시작함
#     print(cnt)

############# 11번 수들의 조합   ############


# def DFS(L, s, sum):
#     global cnt
#     if L == k:
#         if sum % m == 0:
#             cnt += 1
#     else:
#         for i in range(s, n):  ## a리스트를 도는 것이기 때문에 여기 n까지만 돌아야 한다.
#             DFS(L + 1, i + 1, sum + a[i])


# if __name__ == "__main__":
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     m = int(input())
#     cnt = 0
#     DFS(0, 0, 0)
#     print(cnt)

############# 12번 라이브러리를 이용한 순열(수열 추측하기 ) #######
# 라이브러리를 막아놓는 경우가 있으니 기본이 중요하다.특정 조건일때는 라이브러리 안됨


# n, f = map(int, input().split())
# b = [1] * n
# cnt = 0
# for i in range(1, n):
#     b[i] = b[i - 1] * (n - i) / i
# a = list(range(1, n + 1))
# for tmp in it.permutations(a):
#     sum = 0
#     for L, x in enumerate(tmp):
#         sum += x * b[L]
#     if sum == f:
#         for x in tmp:
#             print(x, end=" ")
#         break
########### 13번 라이브러리를 이용한 조합 ############

# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# m = int(input())
# cnt = 0
# for x in it.combinations(a, k):
#     if sum(x) % m == 0:
#         cnt += 1
# print(cnt)
########### 14번 인접행렬 ############
# n, m = map(int, input().split())
# g = [[0] * (n + 1) for _ in range(n + 1)]
# for i in range(m):
#     a, b, c = map(int, input().split())
#     g[a][b] = c

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(g[i][j], end=" ")
#     print()
########### 15번 경로탐색 (그래프 DFS) ############
# def DFS(v):
#     if v == n:
#         cnt += 1
#         for x in path:
#             print(x,end=" ")
#         print()
#     else:
#         for i in range(1, n + 1):
#             if g[v][i] == 1 and ch[i] == 0:
#                 ch[i] = 1
#                 path.append(i)
#                 DFS(i)
#                 path.pop()
#                 ch[i] = 0


# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     g = [[0] * (n + 1) for _ in range(n + 1)]  ##그래프
#     ch = [0] * (n + 1)
#     for i in range(m):
#         a, b = map(int, input().split())
#         g[a][b] = 1
#     cnt = 0
#     path=[]
#     path.append(1)
#     ch[1] = 1
#     DFS(1)
#     print(cnt)
