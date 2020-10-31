def countOfPairs(n,arr):
    dict_={}
    x=set()
    cou=0
    for i in range(0,n):
        w=arr[i]
        dict_[w]=arr.count(w)
        x.add(w)
    for i in x:
        a=dict_[i] 
        if a<=2 and a%2==0:
            cou=cou+a//2 
        elif a<=2 and a%2!=0:
            cou=cou+(a-1)//2

    print(cou)    

countOfPairs(7,[2,2,3,3,4,4,1])   
