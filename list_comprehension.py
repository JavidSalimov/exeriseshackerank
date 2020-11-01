x = int(input())
y = int(input())
z = int(input())
n = int(input())

sss= [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1)]
b=[]
for a in sss:
   
    if sum(a)!=n:
        b.append(a)

print(b)

# https://www.hackerrank.com/challenges/list-comprehensions/problem  serti ile burada tanish ola bilersen