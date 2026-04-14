n=int(input("enter no of process:"))
quantum=int(input("enter quantum number:"))
list1=[]
list2=[]
list3=[]
list4=[]
rem=[]
total_wt=0
wt=[]
wt.append(0)
for i in range(n):
    a=input("enter a process:")
    b=int(input("enter its burst number:"))
    list1.append([a,b])
    rem.append(b)
print(list1)
j=1
s=sum(rem)
while s!=0:
    for i in range(n):
        if list1[i][1]>0:
            if list1[i][1]>quantum:
                s=s-quantum
                print(quantum+wt[j-1])
                wt.append(quantum+wt[j-1])
                list1[i][1]=list1[i][1]-quantum
                print(list1[i])
                list2.append(list1[i][0])
                j+=1
            else:
                s=s-list1[i][1]
                print(list1[i][1]+wt[j-1])
                wt.append(list1[i][1]+wt[j-1])
                list1[i][1]=0
                print(list1[i])
                list2.append(list1[i][0])
                j+=1
    if s==0:
        break
r=1
for i in range(len(list2)):
    list3.append([list2[i],wt[r]])
    r+=1
print(list3)

for i in range(n):
    for j in range(len(list3)):
        if list1[i][0]==list3[j][0]:
            list1[i][1]=list3[j][1]       
print("completion time of each process:",list1)

list4=list1.copy()
for i in range(n):
    list4[i][1]=list1[i][1]-rem[i]
print("waiting time of each process:",list4)

for i in range(n):
    total_wt=total_wt+list4[i][1]
print("total waiting time:",total_wt)
print("average waiting time:",total_wt/n)

q=0
for i in range(len(list2)):
    print(f"process:{list2[i][0]} will start at time : {wt[q]} and end at time : {wt[q+1]}")
    q+=1