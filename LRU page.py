pages = list(map(int, input("enter pages: ").split()))
frame = int(input("enter frames: "))
list1 = []
list2 = []

pagefault = 0
hit = 0

for i in range(len(pages)):
    page = pages[i]
    v1=pages[i-1]
    v2=pages[i-2]
    if page in list1:
        hit += 1
    else:
        pagefault += 1
        if len(list1) < frame:
            list1.append(page)
        else:
           for i in range(0,len(list1)):
               if list1[i]!=v1 and list1[i]!=v2:
                   rem=list1[i]
                   list1.remove(rem)
                   break
           list1.append(page)
    print("elements in the frame:", list1)
    
print("hit:", hit)
print("pagefault:", pagefault)