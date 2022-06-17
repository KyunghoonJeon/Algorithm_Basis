import time

n,k=map(int, input().split())
result=0

start_time=time.time()

while True:
    target=(n//k)*k
    result+=(n-target)
    n=target
    if n<k:
        break
    result+=1
    n//=k
result+=(n-1)
print(result)

end_time=time.time()
print("time :", end_time-start_time)