path=list(map(int,input("enter paths:").split()))
list1=[]
for i in range(len(path)-1):
   total=abs(path[i+1]-path[i])
   list1.append(total)
   print(f"({path[i+1]} - {path[i]}={total})")
   if i!=len(path)-2:
       print("+")

print(f"total distance: {sum(list1)}")
