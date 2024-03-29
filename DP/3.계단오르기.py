import sys

sys.stdin = open("DP/input.txt", "rt")

def DFS(len):
    if dy[len]>0:
        return dy[len]

    if len==1 or len==2:
        return len
    else:
        dy[len]=DFS(len-2)+DFS(len-1)
        return dy[len]
    
if __name__=="__main__":
    n=int(input())
    dy=[0]*(n+1)
    print(DFS(n))