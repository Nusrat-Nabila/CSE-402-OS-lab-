n=int(input("enter no of processes:"))
list1=[]
for i in range(0,n):
    a=input("enter process:")
    b=int(input("enter burst time:"))
    c=int(input("enter priority:"))
    list1.append([a,b,c])
wt=[]
wt.append(0)
list1.sort(key=lambda x:x[2])
for i in range(1,n):
    wt.append(list1[i-1][1]+wt[i-1])
print("average waiting time:",sum(wt)/n)
for i in range(0,n):
    print(f"process{list1[i][0]} start at {wt[i]} and end at {list1[i][1]+wt[i]}")