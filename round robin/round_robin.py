n=int(input("enter no of processes:"))
list1=[]
list2=[]
list3=[]
list4=[]

total_bt=0
for i in range(0,n):
    a=input("enter process:")
    b=int(input("enter burst time:"))
    list1.append([a,b])
    list2.append([a,b])
    list3.append([a,b])
    total_bt=total_bt+b
quantum=int(input("enter the value of quantum:"))


ct=[]
ct.append(0)
j=0
p=[]

while total_bt>0:
 for i in range(len(list1)):
   if list1[i][1]>0:
      if list1[i][1]>quantum:
         ct.append(ct[j]+quantum)
         p.append(list1[i][0])
         list1[i][1]=list1[i][1]-quantum
         total_bt=total_bt-quantum
         j+=1
      else:
         ct.append(list1[i][1]+ct[j])
         p.append(list1[i][0])
         total_bt=total_bt-list1[i][1]
         list1[i][1]=0
         j+=1


for i in range(len(p)):
   list4.append([p[i],ct[i+1]]) 

for i in range(len(list3)):
   for j in range(len(list4)):
      if list3[i][0]==list4[j][0]:
         list3[i][1]=list4[j][1]
print("complation time of each process:",list3)

wt=[]
for i in range(len(list3)):
   t=list3[i][1]-list2[i][1]
   wt.append(t)
   
print(wt) 
print("average waiting time:",sum(wt)/n)

for i in range(len(p)):
    print(f"process {p[i]} started at {ct[i]} and end at {ct[i+1]}")
