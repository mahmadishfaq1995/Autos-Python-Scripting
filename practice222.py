arr = [1, 2, 3, 4, 2, 7, 8, 8, 3];
length=len(arr)-1
exists = 0
arrb=[];
print("Duplicate elements in given array: ");
# Searches for duplicate element
for i in range(0, length):
    key = arr[i]
    for j in range(i + 1, length):
        if arrb[j]==key:
             exists = 1
        else:
            exists = 0
    if exists == 1:
        arrb[j]=arr[i]
        j+=1
for i in range(0, j):
    print(arrb[i])


