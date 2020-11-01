l=[]
s=[]
for i in range(int(input())):

        ll=[]
        name = input()
        score = float(input())
        ll.append(name)
        ll.append(score)
        
        l.append(ll)
        if score not in s:
            s.append(score)
        
l.sort(key=lambda x: x[1])

s.sort()
print(s)




lll=[]
for i in l:
    if i[1]==highdeg:
        lll.append(i[0])

lll.sort()
for i in lll:
    print(i)       



# n=int(input())
# arr=[[input(),float(input())] for _ in range(0,n)]
# arr.sort(key=lambda x: (x[1],x[0]))
# names = [i[0] for i in arr]
# marks = [i[1] for i in arr]
# min_val=min(marks)
# while marks[0]==min_val:
#     marks.remove(marks[0])
#     names.remove(names[0])    
# for x in range(0,len(marks)):
#     if marks[x]==min(marks):
#         print(names[x])    