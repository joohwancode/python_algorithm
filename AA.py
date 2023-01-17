import sys

sys.stdin = open("input.txt", "rt")

############ 1번 최대점수 구하기 (DFS) ################
# def DFS(L, sum, time):
#     global res
#     if time > m:
#         return
#     if L == n:
#         if sum > res:
#             res = sum
#     else:
#         DFS(L + 1, sum + pv[L], time + pt[L])
#         DFS(L + 1, sum, time) ##현재 문제를 안풀수도 있음


# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     pv = list()
#     pt = list()
#     for i in range(n):
#         a, b = map(int, input().split())
#         pv.append(a)
#         pt.append(b)
#     res = -2147000000
#     DFS(0, 0, 0)
#     print(res)

############ 2번 휴가 (DFS) ################
# def DFS(L, sum):
#     global res
#     if L == n + 1:
#         if sum > res:
#             res = sum
#     else:
#         if L + T[L] <= n + 1:
#             DFS(L + T[L], sum + P[L])
#         DFS(L + 1, sum
# if __name__ == "__main__":
#     n = int(input())
#     T = list()
#     P = list()
#     for i in range(n):
#         a, b = map(int, input().split())
#         T.append(a)
#         P.append(b)
#     res = -2147000000
#     T.insert(0, 0)  ###인덱스 1일을 맞춰주기 위해서 하는 것이다.
#     P.insert(0, 0)
#     DFS(1, 0)
#     print(res)

############ 3번 양팔저울  (DFS) ################


# if __name__ == "__main__":
#     n = int(input())

############ 4번 동전 바꿔주기  (DFS) ################


# def DFS(L, sum):
#     global cnt
#     if L == K:
#         if sum == T:
#             cnt += 1
#     else:
#         for i in range(cn[L] + 1):  ##여기를 계속 틀렷음 cn[l]로 했다.
#             DFS(L + 1, sum + (cv[L] * i))


# if __name__ == "__main__":
#     T = int(input())
#     K = int(input())
#     cv = list()
#     cn = list()
#     for i in range(K):
#         a, b = map(int, input().split())
#         cv.append(a)
#         cn.append(b)
#     cnt = 0
#     DFS(0, 0)
#     print(cnt)
############ 5번 동전 분배하기  (DFS) ################


def DFS(L):
    global res
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()  ##중복을 방지하는 코드임
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L + 1)
            money[i] -= coin[L]


if __name__ == "__main__":
    n = int(input())
    coin = []
    money = [0] * 3
    res = 2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)
