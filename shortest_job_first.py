n=int(input("enter no of process:"))
list2=[]
list3=[]
list4=[]
for i in range(n):
     list1=[]
     p=input("enter a process:")
     b=int(input("enter that process's burst time:"))
     list1.append(p)
     list1.append(b)
     list2.append(list1)
print(list2)
for i in range(n):
    list3.append(list2[i][1])
list3.sort()
j=0
for i in range(n):
    k=0
    while j<n and k<n:
     if (list3[j])==(list2[k][1]):
        if list2[k] not in list4:
         list4.append(list2[k])
         j+=1
         break
     else:
        k+=1
print(list4)  
wt=[]
wt.append(0)
total_wt=0
for i in range(1,n):
    wt.append(list4[i-1][1]+wt[i-1])
    total_wt=total_wt+wt[i]
print(wt)
print(total_wt)
print(total_wt/n)
for i in range(n):
    print(f"process:{list4[i][0]} will start at {wt[i]} and will end at {wt[i]+list4[i][1]}")
     
    

   
