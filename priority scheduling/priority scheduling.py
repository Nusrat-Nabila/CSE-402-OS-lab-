n=int(input("enter no of process:"))
list1=[]
list2=[]
list3=[]
for i in range(n):
    a=input("enter a process:")
    b=int(input("enter its burst number:"))
    c=int(input("enter its priority number:"))
    list1.append([a,b,c])
print(list1)
for i in range(n):
    list2.append(list1[i][2])
list2.sort()

k=0
for i in range(n):
 j=0
 while j<n and k<n:
    if list2[k]==list1[j][2]:
        list3.append(list1[j])
        k+=1
        break
    else:
        j+=1 
print(list3) 
wt=[]
wt.append(0)
total_wt=0
for i in range(1,n):
    wt.append(wt[i-1]+list3[i-1][1])
    total_wt=total_wt+wt[i]
print("waiting time of each process:",wt)
print("total waiting time:",total_wt)
print("average waiting time:",total_wt/n)
for i in range(n):
    print(f"process:{list3[i][0]} will start at time : {wt[i]} and end at time : {wt[i]+list3[i][1]}")
