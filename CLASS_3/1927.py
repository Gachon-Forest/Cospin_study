import heapq
import sys
n=int(sys.stdin.readline())
heap=[]

for _ in range(n):
    a=int(sys.stdin.readline())
    if a==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,a)