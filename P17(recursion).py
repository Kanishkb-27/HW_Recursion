count1=0
def myfunction1(n):
    global count1
    count1+=1
    if n<=0:
        return
    for i in range(0,n+1):
        pass
    myfunction1(n//2)
    myfunction1(n//3)
for i in [1,2,4,6,8]:
    count1=0
    myfunction1(i)
    print(f"n={i}, calls={count1}")
print("\n")
print("\n")
count2=0
def myfunction2(n):
    global count2
    count2+=1
    if(n<=1):
        return
    myfunction2(n-1)
for i in range(1,6):
    count2=0
    myfunction2(i)
    print(f"n={i}, calls={count2}")