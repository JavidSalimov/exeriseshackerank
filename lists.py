if __name__ == '__main__':
    N = int(input())
    a=[]

    for n in range(N):
        z=list(input().split())
        if z[0]=='insert':
            a.insert(int(z[1]),int(z[2]))
        elif z[0]=='print':
            print(a) 
        elif z[0]=='remove':
            a.remove(int(z[1])) 
        elif z[0]=='append':
            a.append(int(z[1])) 
        elif z[0]=='sort':
            a.sort()  
        elif z[0]=='pop':
            a.pop()
        elif z[0]=='reverse':
            a.reverse()    
#  https://www.hackerrank.com/challenges/python-lists/problem bu linkde tapshiriqa baxa bilersen