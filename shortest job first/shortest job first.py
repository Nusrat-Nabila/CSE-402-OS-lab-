n=int(input("enter no of process:"))
list1=[]
for i in range(0,n):
    a=input("enter process:")
    b=int(input("burst time:"))
    list1.append([a,b])
list1.sort(key=lambda x:x[1]) # here (key}<--Specifies a function that determines the value used for comparison during sorting. and {lambda x: x[1]}<-- A small anonymous function that returns the second element of each item in the list.
wt=[]
wt.append(0)
for i in range(1,n):
    t=list1[i-1][1]+wt[i-1]
    wt.append(t)
total_wt=sum(wt)
print("average waiting time:",total_wt/n)
for i in range(0,n):
    print(f"process{list1[i][0]} started at {wt[i]} and end at { list1[i][1]+wt[i]}")
 