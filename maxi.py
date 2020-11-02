n=list(map(int,input().split()))

list_of_inputs=[]

for i in range(0,n[0]):
    stre=list(map(int,input().split()))
    list_of_inputs.append(stre)

maxx=[]
for i in list_of_inputs:
    maxx.append(max(i))

def fmy(arr,n):
    # s=[i*i for i in arr]
    # z=sum([i*i for i in arr])
    # cavab=sum([i*i for i in arr])%n
    return sum([i*i for i in arr])%n



print(fmy(maxx,n[1]))


# print(list_of_inputs)

# print(maxx)
# bu helli yoludur
# from itertools import product
# K,M = map(int,input().split())
# N = (list(map(int,input().split()))[1:] for _ in range(K))
# results = map(lambda x: sum(i**2 for i in x)%M,product(*N))
# print(max(results))

# https://www.hackerrank.com/challenges/maximize-it/problem