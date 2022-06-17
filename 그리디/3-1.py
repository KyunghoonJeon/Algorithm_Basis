n=int(input("거스름돈: "))
cnt=0
coins=[500,100,50,10]
for coin in coins:
    cnt+=n//coin
    n%=coin
print(cnt)