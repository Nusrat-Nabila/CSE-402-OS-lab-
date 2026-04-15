list1=list(map(int,input("enter path:").split()))
list2=[]
head=int(input("enter head:"))
total_dis=0

head1=head
if head not in list1:
    list1.append(head)
    

while len(list1)>0:
  if list1 == [head1]:
    list1.remove(head1)
    break

  for i in range(len(list1)):
      if head1!=list1[i]:
        list2.append([list1[i],abs(head1-list1[i])])
        
  list2.sort(key=lambda x:x[1])
  print(list2)
  print(f"{head1}-->{list2[0][0]}")
  total_dis=total_dis+list2[0][1]
  
  if head1 in list1:
    list1.remove(head1)
  head1=list2[0][0]
  list2.clear()
  print(total_dis)   
