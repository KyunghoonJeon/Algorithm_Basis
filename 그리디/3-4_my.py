import time

n,m=map(int, input().split())

start_time=time.time()

cnt=0
while True:
    if n==1:
        break
    elif n%m==0:
        n//=m
        cnt+=1
    elif n%m!=0:
        n-=1
        cnt+=1
print(cnt)

end_time=time.time()
print("time :", end_time-start_time)