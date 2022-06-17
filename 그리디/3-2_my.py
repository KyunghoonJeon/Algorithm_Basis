n, m, k=map(int, input().split())
data=list(map(int, input().split()))

data.sort(reverse=True)
first=data[0]
second=data[1]

big_num=0
# while m>=0:
#     for i in range(k):
#         big_num+=first
#         m-=1
#     big_num+=second
#     m-=1
# print(big_num)
while True:
    for i in range(k):
        if m==0:
            break
        big_num+=first
        m-=1
    if m==0:
        break
    big_num+=second
    m-=1
print(big_num)