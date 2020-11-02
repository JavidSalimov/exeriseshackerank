# Complete the solve function below.
# s=input()
# def solve(s):
#     a=list(s.split(" "))

#     b=[]
#     for i in a:
#         c=i
#         if  not c[0].isalpha() and not c=="":
#             b.append(c)
#         if c=="":
#             b.append(" ") 
        
#         else:
#             b.append(c.capitalize())    
        

    # return a
#     return " ".join(b)  

# print(solve(s))

def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s

