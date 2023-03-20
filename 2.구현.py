# # import sys

# # # sys.stdin = open("input.txt", "rt")


# n, k = list(map(int, input().split()))
# cnt = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         cnt += 1
#     if cnt == k:
#         print(i)
#         break
# else:
#     print(-1)


# n, k = list(map(int, input().split()))
# cnt = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         cnt += 1
#     if cnt == k:
#         print(i)
#         break
# else:
#     print(-1)


# import sys

# sys.stdin = open("input.txt", "rt")

# ## 2번 다시해야함
# # T = int(input())
# # for i in range(T):
# #     n, s, e, k = map(int, input().split())
# #     a = list(map(int, input().split()))
# #     a = a[s - 1 : e]
# #     a.sort()
# #     print("#%d %d" % (i + 1, a[k - 1]))


# T = int(input())
# for i in range(T):
#     N, s, e, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     a = a[s - 1, k]
#     a.sort()
#     print("#%d %d" % (i + 1, a[k - 1]))
# # 3번 문제
# # n, k = map(int, input().split())
# # a = list(map(int, input().split()))
# # ##3개를 추출해서 다 더한다. 그중에 3번째로 큰것
# # # set은 중복을 제거한다.
# # res = set()
# # # i+1 다음으로 돌아야 한다. 다시
# # ##set은 add를 쓴다.
# # for i in range(n):
# #     for j in range(i + 1, n):
# #         for m in range(j + 1, n):
# #             res.add(a[i] + a[j] + a[m])
# # ##k번째기 때문에 일단 sort를 해야한다.근데 k번째로 큰 수기 때문에 내림차순을 해야한다.
# # ##set은 sort가 안되기 때문에 리스트로 만들어 주어야 한다.
# # res = list(res)

# # res.sort(reverse=True)
# # print(res[k - 1])

# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# ##중복을 제거해야 한다.
# res = set()
# for i in range(n):
#     for j in range(i + 1, n):
#         for m in range(j + 1, n):
#             res.add(a[i] + a[j] + a[m])
# ##set함수는 sort가 안됨

# res = list(res)
# res.sort(reverse=True)
# print(res[k - 1])

# ##


# ##최소값을 구하기
# # 6
# ##4번 문제임


# # n = int(input())
# # a = list(map(int, input().split()))

# # 평균을 어서 구한다.
# # avg = round(sum(a) / n)


# # ##최소값을 구하기


# # ##평균에 가까운 숫자 ?????
# # for i in a:
# #     if i >= avg:
# #         print(enumerate(i))


# # ##최소값을 구하기

# # arr=[]
# # arrMin
# # n = int(input())
# # a = list(map(int, input().split()))
# # ave = round(sum(a) / n)
# # 파이썬의 round는 round half even 방식을 택한다. 그렇기 때문에 다르게 표현해야 한다.
# # a = 66.4
# # a = a + 0.5
# # a = int(a)
# # print(a)
# # min = 2147000000
# # ##거리가 평균하고 가까워야 한다 .
# # for idx, x in enumerate(a):
# #     ##일단 거리를 만들어서 계산해줘야 한다.
# #     tmp = abs(ave - x)
# #     if tmp < min:
# #         min = tmp
# #         score = x
# #         res = idx + 1
# #     ##중복제거해주기 거리 같을때 큰걸 나오게 한다.
# #     elif tmp == min:
# #         if x > score:  ## = 같다라는 이 조건에 들어가면 안된다 .그러면 중복 값중 마지막 까지 가게 된다.
# #             score = x
# #             res = idx + 1
# # print(ave, res)

# ##평균 구하기
# n = int(input())
# a = list(map(int, input().split()))
# ave = round(sum(a) / n)
# min = 2146000000
# for idx, x in enumerate(a):
#     tmp = abs(ave - x)
#     if tmp < min:
#         min = tmp
#         score = x  ## 스코어를 좀 비교해 주어야 한다.
#         res = idx + 1  # 인덱스는 1부터 시작하기 때문에
#     ## 중복을 없애 주어야 한다.
#     elif tmp == min:
#         if x > score:
#             score = x
#             res = idx + 1
# print(ave, res)
# ## 5번 정다면체
# # n, m = map(int, input().split())
# # cnt = [0] * (n + m + 3)  ## 넉넉하게 3도 더해준다.
# # ## 돌면서
# # max = -2147000000
# # for i in range(1, n + 1):
# #     for j in range(1, m + 1):
# #         cnt[i + j] += 1
# # ###이제 최댓값을 찾아야 한다.
# # for i in range(n + m + 1):
# #     if cnt[i] > max:
# #         max = cnt[i]

# # ##중복되는 값이 있으면 같이 출력한다.
# # for i in range(n + m + 1):
# #     if cnt[i] == max:
# #         print(i, end=" ")

# ## 2번째 구현
# n, m = map(int, input().split())
# cnt = [0] * (n + m + 3)  ## 넉넉하게 3개로 잡는다.
# max = -2147000000
# for i in range(1, n + 1):  # 열
#     for j in range(1, m + 1):
#         cnt[i + j] += 1
# ##최댓값을 뽑아내야 한다.

# for i in range(n + m + 1):
#     if cnt[i] > max:
#         max = cnt[i]
# for i in range(n + m + 1):
#     if cnt[i] == max:
#         print(i, end=" ")


# # 6번 자릿수의 합
# # 2가지 방법이 있음


# # n = int(input())
# # a = list(map(int, input().split()))


# # def digit_sum(x):
# #     sum = 0
# #     while x > 0:
# #         sum += x % 10
# #         x = x // 10  # 대입한다는 느낌임
# #     return sum


# # ##max 값을 찾아준다.
# # max = -2467000000
# # for x in a:
# #     tot = digit_sum(x)
# #     if tot > max:
# #         max = tot
# #         res = x
# # print(res)


# ## 2번째 방법 string을 int로 바꾸는 것


# # n = int(input())
# # a = list(map(int, input().split()))


# # def digit_sum(x):
# #     sum = 0
# #     for i in str(x):
# #         sum += int(i)
# #     return sum


# # max = -2147000000
# # for x in a:
# #     tot = digit_sum(x)
# #     if tot > max:
# #         max = tot
# #         res = x
# # print(res)

# ## 7번 소수 구하기
# ##에라토스 테네스체
# # n = int(input())
# # ch = [0] * (n + 1)

# # cnt = 0
# # for i in range(2, n + 1):
# #     if ch[i] == 0:
# #         cnt += 1
# #     ##돌면서 체크를 해준다.맨 마지막은 step이다.
# #     for j in range(i, n + 1, i):
# #         ch[j] = 1
# # print(cnt)
# ##8번 뒤집은 소수
# ##자리수 뒤집는 것

# # n = int(input())
# # a = list(map(int, input().split()))

# # ##0이 있으면 걍 무시해 버리는 것이다.
# # def reverse(x):
# #     res = 0
# #     ##0보다 클때만 참이 되는 것임
# #     while x > 0:
# #         t = x % 10  ## x의 1의자리 숫자가 t가 된다.
# #         res = res * 10 + t
# #         x = x // 10
# #     return res


# # def isPrime(x):
# #     if x == 1:  ## 1이면 안됨 소수가 아님
# #         return False
# #     for i in range(2, x // 2 + 1):  ### 절반 까지만 돌아도 된다.
# #         if x % i == 0:
# #             return False
# #     else:  ## 정상적으로 종료되면 retuen  true
# #         return True


# # for x in a:
# #     tmp = reverse(x)
# #     if isPrime(tmp):
# #         print(tmp, end=" ")


# ##9번 주사위 게임
# # n = int(input())
# # res = 0
# # for i in range(n):
# #     tmp = input().split()
# #     tmp.sort()  ##오름차순으로 바꿔줌
# #     ##지금은 문자기 때문에 정수화 시켜야함
# #     a, b, c = map(int, tmp)
# #     ##변수 하나에 기준을 줘야 한다.
# #     if a == b and b == c:ㅁ
# #         money = 10000 + (a * 1000)
# #     elif a == b or a == c:
# #         money = 1000 + (a * 100)
# #     elif b == c:
# #         money = 1000 + (b * 100)
# #     else:
# #         money = c * 100
# #     ##최댓값 구하기
# #     if money > res:
# #         res = money
# ##리스트 3개를 받는다.
# # print(res)
# ## 10번 문제 풀기
# n = int(input())
# ##연속되는 숫자가 나오고 그것을 받아준다.
# a = list(map(int, input().split()))
# ##점수를 합해야함
# ##가중치를 줘야한다.
# sum = 0
# cnt = 0
# for x in a:
#     if x == 1:
#         cnt += 1
#         sum += cnt
#     else:
#         cnt = 0
# print(sum)
