# import sys

# sys.stdin = open("DP/input.txt", "rt")


# def DFS(len):
#     ##가지치기를 해줘야 한다. 구해져 있으면 가지뻗지 말고 바로 리턴해라  
#     if dy[len]>0:
#         return dy[len]
#     if len==1 or len==2:
#         return len
#     else:
#         dy[len]=DFS(len-1)+DFS(len-2)
#         return dy[len]

# if __name__=="__main__":
#     n=int(input())
#     dy=[0]*(n+1)
#     print(DFS(n))