def palindrome(str):
    flag = True
    if len(str) > 1:
        e = len(str) - 1
    if len(str) == 1:
        e = 0
    s = 0
    for i in range(s, e):
        if str[s] == str[e]:
            s += 1
            e -= 1
            i += 1
            flag = True
        else:
            flag = False
    return flag


pw = palindrome(str='ahmad')
print(pw)


def sum(number):
    result = 0
    while number > 0:
        rem = number % 10
        result = rem + result
        number = int(number / 10)
    print(result)
#
#
sum(5257)

#
# def checkPalindrome(inputString):
#     length = len(inputString) - 1
#     endpoint = length
#     staringpoint = 0
#     for i in range(staringpoint, endpoint):
#         if inputString[staringpoint] == inputString[endpoint]:
#             staringpoint += 1
#             endpoint -= 1
#             i += 1
#             output = True
#         else:
#             output = False
#     return output

#Reverse string
stri='i love pakistan'
stri.partition(' ')
partition=stri.partition(' ')
reversestr=partition[2]+" "+partition[1]+" "+partition[0]
print(reversestr)

#Swapping two variables without uisng third variable
x = 5.4
y = 10.3
x = x + y  # x = 15.7, y = 10.3
y = x - y  # x = 15.7, y = 5.4
x = x - y  # x = 10.3, y = 5.4
print("After swapping: ")
print("Value of x : ", x, " and y : ", y)
print( "value of x : "+str(y)+" value of y: "+str(x))

#make array unique
cars=['honda','toyota','kia','honda','toyota']
carsset=set(cars)
listt = list(carsset)
print(carsset)
print(listt)

#make array unique using loop

cars=['kia','honda','toyota','honda','toyota']
output = set()
for i in cars:
    output.add(i)
print(output)

arr = [1, 2, 3, 4, 2, 7, 8, 8, 3];

print("Duplicate elements in given array: ");
# Searches for duplicate element
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] == arr[j]):
            print(arr[j]);


arr = [1, 2, 3, 4, 2, 7, 8, 8, 3];
exists = 0
print("Duplicate elements in given array: ");
# Searches for duplicate element
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] == arr[j]):
            arr[i]=arr[]

str = "Python" # initial string
reversedString=[]
index = len(str) # calculate length of string and save in index
while index > 0:
    reversedString += str[ index - 1 ] # save the value of str[index-1] in reverseString
    index = index - 1 # decrement index
print(reversedString) # reversed string