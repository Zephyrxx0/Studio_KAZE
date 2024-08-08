n = int(input("Enter the number of elements: "))
list1 = []
for i in range(0,n):
    element = int(input()) 
    list1.append(element)
print(list1)

key = int(input("Enter key element: "))

for element in list1:
    
    if key == element:
        idx = list1.index(element)
        break

print(idx)















