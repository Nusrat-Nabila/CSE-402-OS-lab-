n=int(input("enter no of processes:"))
list1=[]
for i in range(0,n):
    a=input("enter process:")
    b=int(input("enter burst time:"))
    list1.append([a,b])
wt=[]
wt.append(0)

for i in range(1,n):
    t=list1[i-1][1]+wt[i-1]
    wt.append(t)
total_wt=sum(wt)
ave_wt=total_wt/n
print("average waiting time:",ave_wt)
for i in range(0,n):
    print(f"process{list1[i][0]} started at {wt[i]} and end at {wt[i]+list1[i][1]}")
    
    