n = int(input("Enter the number of elements: "))
list1 = []
for i in range(0,n+1):
    list1 = input() 
    list1.append(list1)

key = int(input("Enter key element: "))

for element in list1:
    if key == element:
        idx = element.index()
        break

print(idx)
















