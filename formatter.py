def print_formatted(number):
    # your code goes here
    
    for n in range(1,number+1):

        z=(len(f'{(bin(number))[2:]}'))*" " 

        print(f"{n}{z}{oct(n)[2:]}{z}{(hex(n)[2:]).capitalize()}{z}{(bin(n))[2:]}")

       
        


   
    
print_formatted(17)    
    