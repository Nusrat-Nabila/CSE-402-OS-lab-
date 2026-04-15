#!/usr/bin/python3
pages=list(map(int,input("enter pages:").split()))
frame=int(input("enter frames:"))
list1=[0]*frame
pagefault=0
hit=0
for page in pages:
    if len(list1)<frame:
       if page not in list1:
        list1.append(page)
        print(list1)
        pagefault+=1
       else:
           hit+=1 
    else:
        if page not in list1:
            list1.pop(0)
            list1.append(page)
            print(list1)
            pagefault+=1
        else:
            hit+=1
print("hit:",hit)
print("miss:", pagefault)            