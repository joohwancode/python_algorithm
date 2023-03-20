
# import sys
# from collections import deque
# sys.stdin = open("input.txt", 'r')

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
# def new_func(__name__):
#     def DFS(L):
#         global res
#         if L==n:
#             cha=max(money)-min(money)
#             if cha<res:
#                 tmp=set()
#                 for x in money:
#                     tmp.add(x)
#                 if len(tmp)==3: ##세사람의 총액이 달라야 한다는 조건이 있다.
#                     res=cha
#         else:
#             for i in range(3):
#                 money[i]+=coin[L]
#                 DFS(L+1)
#                 money[i]-=coin[L] ###다시 돈을 빼주는 상황이 된다.


#     if __name__ == "__main__":
#         n = int(input())
#         coin = []
#         money=[0]*3
#         res=2147000000
#         for _ in range(n):
#             coin.append(int(input()))
#         DFS(0)
#         print(res)
# def DFS(L,P):
#     global cnt
#     if L==n:
#         cnt+=1
#         for j in range(P):
#             print(chr(res[j]+64),end=" ")
#         print()
#     else:
#         for i in range(1,27):
#             if code[L]==i:
#                 res[P]=i
#                 DFS(L+1,P+1)
#             elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
#                 res[P]=i
#                 DFS(L+2,P+1)

# if __name__ == "__main__":
#     code=list(map(int,input()))
#     n=len(code)
#     code.insert(n,-1)
#     res=[0]*(n+3) ## 이걸 왜 이렇게 하는거야 씌부레 ## 뒤에 인덱스 까지 미리 볼 수 있도록 하는 것 같다 .
#     cnt=0
#     DFS(0,0)
# print(cnt)

########## 7.송아지 찾기 ################

# MAX = 10000
# ch = [0]*(MAX+1)
# dis = [0]*(MAX+1)
# n, m = map(int, input().split())
# ch[n] = 1
# dis[n] = 0
# dQ = deque()
# dQ.append(n)  # 처음 값을 넣는다.
# while dQ:
#     now = dQ.popleft()  # 제일 앞에 있는 값을 뽑음
#     if now == m:
#         break

#     for next in (now+1, now-1, now+5):
#         if 0 < next < MAX:
#             if ch[next] == 0:
#                 dQ.append(next)
#                 ch[next] = 1
#                 dis[next] = dis[now]+1  # 자기 부모에서 하나 더하는 것 now가 부모이다.
# print(dis[m])

####### 8.사과나무 #######
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# n = int(input())
# a = [list(map(int, input().split()))for _ in range(n)]
# ch = [[0]*n for _ in range(n)]  # 방문하는 거 체크
# 합계를 만들어야 한다.
# sum = 0
# Q = deque()
# ch[n//2][n//2] = 1
# sum += a[n//2][n//2]
# Q.append((n//2, n//2))
# L = 0
# while True:
#     if L == n//2:
#         break
#     # 하나를 꺼내서 퍼져나간다.
#     size = len(Q)
#     for i in range(size):
#         tmp = Q.popleft()
#         for j in range(4):  # 사방을 돈다 .
#             x = tmp[0]+dx[j]
#             y = tmp[1]+dy[j]
#             if ch[x][y] == 0:
#                 sum += a[x][y]
#                 ch[x][y] = 1
#                 Q.append((x, y))
#     L += 1
# print(sum)

######## 미로의 최단 경로 통로 #########
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# board = [list(map(int, input().split())) for _ in range(7)]
# dis = [[0]*7 for _ in range(7)]
# Q = deque()
# Q.append((0, 0))
# board[0][0] = 1
# while Q:
#     tmp = Q.popleft()
#     for i in range(4):
#         x = tmp[0]+dx[i]
#         y = tmp[1]+dy[i]
#         if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:  # 0이여야 통로가 됨
#             board[x][y] = 1  # 체크를 해줘야 한다.
#             dis[x][y] = dis[tmp[0]][tmp[1]]+1
#             Q.append((x, y))
# if dis[6][6] == 0:  # 도착하지 못햇다면
#     print(-1)
# else:
#     print(dis[6][6])

### 미로탐색 dfs ####
##가는 방법의 수 
# import sys 
# sys.stdin=open("input.txt","r")
# dx=[-1,0,1,0]
# dy=[0,1,0,-1]

# def DFS(x,y):
#     global cnt
#     if x==6 and y==6:
#         cnt+=1
#     else:
#         for i in range(4):
#             xx=x+dx[i]
#             yy=y+dy[i]
#             if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0:
#                 board[xx][yy]=1
#                 DFS(xx,yy)
#                 board[xx][yy]=0
                
# if __name__=="__main__":
#     board=[list(map(int,input().split()))for _ in range(7)]
#     cnt=0
#     board[0][0]=1
#     DFS(0,0)
#     print(cnt)


# dx=[-1,0,1,0]
# dy=[0,1,0,-1]

# def DFS(x,y):
#     global cnt
#     if x==ex and y==ey:
#         cnt+=1
#     else:
#         for k in range(4):
#             xx=x+dx[k]
#             yy=y+dy[k]
#             if 0<=xx<n and 0<=yy<n and board[xx][yy]>board[x][y]:
#                 ch[xx][yy]=1
#                 DFS(xx,yy)
#                 ch[xx][yy]=0

# if __name__=="__main__":
#     n=int(input())
#     board=[[0]*n for _ in range(n)]
#     ch=[[0]*n for _ in range(n)]
#     max=-2147000000
#     min=2147000000
#     for i in range(n):
#         tmp=list(map(int,input().split()))
#         for j in range(n):
#             if tmp[j]<min:
#                 min=tmp[j]
#                 sx=i
#                 sy=j
#             if tmp[j]>max:
#                 max=tmp[j]
#                 ex=i
#                 ey=j
#             board[i][j]=tmp[j]
#     ch[sx][sy]=1
#     cnt=0
#     DFS(sx,sy)
#     print(cnt)    

######12. 단지 번호 붙이기 
# dx=[0,1,0,-1]
# dy=[1,0,-1,0]
# def DFS(x,y):
#     global cnt 
#     cnt+=1
#     board[x][y]=0
#     for i in range(4):
#         xx=x+dx[i]
#         yy=y+dy[i]
#         if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
#             DFS(xx,yy)

# if __name__ =="__main__":
#     n=int(input())
#     board=[list(map(int,input()))for _ in range(n)]
#     res =[]
#     for i in range(n):
#         for j in range(n):
#             if board[i][j]==1:
#                 cnt =0
#                 DFS(i,j)
#                 res.append(cnt)

#     print(len(res))
#     res.sort()
#     for x in res:
#         print(x)
######13. 섬나라 아일랜드 ########
# import sys 
# sys.stdin=open("input.txt","r")
# from collections import deque
# dx=[-1,-1,0,1,1,1,0,-1]
# dy=[0,1,1,1,0,-1,-1,-1]

# n=int(input())
# board=[list(map(int,input().split())) for _ in range(n)]
# cnt=0
# Q=deque()
# for i in range(n):
#     for j in range(n):
#         if board[i][j]==1:
#             board[i][j]=0
#             Q.append((i,j))
#             while Q:
#                 tmp=Q.popleft()
#                 for k in range(8):
#                     x=tmp[0]+dx[k]
#                     y=tmp[1]+dy[k]
#                     if 0<=x<n and 0<= y<n and board[x][y]==1:
#                         board[x][y]=0
#                         Q.append((x,y))
#             cnt+=1
# print(cnt)

######14. 안전영역 ########
# dx=[-1,0,1,0]
# dy=[0,1,0,-1]
# sys.setrecursionlimit(10**6) ## 재귀 리밋을 해줘야지 백준사이트에서 가능 
# def DFS(x,y,h):
#     ch[x][y]=1
#     for i in range(4):
#         xx=x+dx[i]
#         yy=y+dy[i]
#         if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h:
#             DFS(xx,yy,h)


# if __name__ =="__main__":
#     n=int(input())
#     cnt=0
#     res=0
#     board=[list(map(int,input().split())) for _ in range(n)]
#     for h in range(100):
#         ch=[[0]*n for _ in range(n)]
#         cnt=0  ## 높이가 바뀌면 다시 해야 함 
#         for i in range(n):
#             for j in range(n):
#                 if ch[i][j]==0 and board[i][j]>h:
#                     cnt+=1
#                     DFS(i,j,h)
#         res=max(res,cnt)
#         if cnt == 0 :
#             break
#     print(res)

# dx=[-1,0,1,0]
# dy=[0,1,0,-1]
# n,m =map(int,input().split())
# board=[list(map(int,input().split()))for _ in range(m)]
# Q=deque()
# dis=[[0]*n for _ in range(m)]
# for i in range(m):
#     for j in range(n):
#         if board[i][j]==1:
#             Q.append((i,j))
# while Q:
#     tmp=Q.popleft()
#     for i in range(4):
#         xx=tmp[0]+dx[i]
#         yy=tmp[1]+dy[i]
#         if 0 <=xx<m and 0<=yy<n and board[xx][yy]==0:
#             board[xx][yy]=1
#             dis[xx][yy]=dis[tmp[0]][tmp[1]]+1
#             Q.append((xx,yy))
# flag=1
# for i in range(m):
#     for j in range(n):
#         if board[i][j]==0:
#             flag=0
# result=0
# if flag==1:
#     for i in range(m):
#         for j in range(n):
#             if dis[i][j]> result:
#                 result=dis[i][j]
#     print(result)
# import sys 
# sys.stdin=open("input.txt","r")
# def DFS(x, y):
#     ch[x][y]=1
#     if x==0:
#         print(y)
#     else:
#         if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
#             DFS(x, y-1)
#         elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
#             DFS(x, y+1)
#         else:
#             DFS(x-1, y)

# board=[list(map(int,input().split())) for _ in range(10)]
# ch=[[0]*10 for _ in range(10)]
# for y in range(10):
#     if board[9][y]==2:
#         DFS(9, y)
# import sys
# sys.stdin=open("input.txt", "r")
# def DFS(x, y):
#     ch[x][y]=1
#     if x==0:
#         print(y)
#     else:
#         if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
#             DFS(x, y-1)
#         elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
#             DFS(x, y+1)
#         else:
#             DFS(x-1, y)


# board=[list(map(int, input().split())) for _ in range(10)]
# ch=[[0]*10 for _ in range(10)]
# for y in range(10):
#     if board[9][y]==2:
#         DFS(9, y)

# def DFS(x,y):


# if __name__ =="__main__":
#     n,m=map(int,input().split())
#     board=[list(map(int,input().split())) for _ in range(n)]
#     hs=[]
#     pz=[]
#     cb=[0]*m
#     res=21470000000
#     for i in range(n):
#         for j in range(n):
#             if board[i][j]==1:
#                 hs.append((i,j))
#             elif board[i][j]==2:
#                 pz.append((i,j))
#     DFS(0,0)