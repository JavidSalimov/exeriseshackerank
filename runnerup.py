n = int(input())
arr = list(map(int, input().split()))

# print(n)
# print(arr) 
x= set()
for i in range(n):
    x.add(arr[i])

z=list(x)
z.sort()  
print(z[len(z)-2])