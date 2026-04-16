pages = list(map(int, input("enter pages: ").split()))
frame = int(input("enter frames: "))
list1 = []
list2 = []

pagefault = 0
hit = 0

for i in range(len(pages)):
    page = pages[i]
    if page in list1:
        print("elements in the frame:", list1)
        hit += 1
    else:
        pagefault += 1

        if len(list1) < frame:
            list1.append(page)
        else:
            future = pages[i + 1:]
            list2.clear()

            for val in list1:
                if val in future:
                    list2.append([val, future.index(val)])
                else:
                    # If the page is not used again, replace it immediately
                    list2.append([val, float('inf')])

            # Select the page used farthest in the future
            list2.sort(key=lambda x: x[1])
            v = list2[-1][0]

            list1.remove(v)
            list1.append(page)

        print("elements in the frame:", list1)

print("hit:", hit)
print("pagefault:", pagefault)