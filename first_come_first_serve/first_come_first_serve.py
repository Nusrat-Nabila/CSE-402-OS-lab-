n=int(input("enter no of process:"))
list1=[]
for i in range(n):
     p=input("enter a process:")
     b=int(input("enter that process's burst time:"))
     list1.append([p,b])
print(list1)  
wt=[]
wt.append(0)
total_wt=0
for i in range(1,n):
    wt.append(list1[i-1][1]+wt[i-1])
    total_wt=total_wt+wt[i]
print(wt)
print(total_wt)
print(total_wt/n)
for i in range(n):
    print(f"process:{list1[i][0]} will start at {wt[i]} and will end at {wt[i]+list1[i][1]}")
     
    

   