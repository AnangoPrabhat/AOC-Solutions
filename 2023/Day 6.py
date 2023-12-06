#part 1: I hardcoded the 4 inputs. Assign a to h with the inputs.
a,b,c,d=60,94,78,82
e,f,g,h=475,2138,1015,1650
p=1
for i in range(4):
    u=[a,b,c,d][i]
    v=[e,f,g,h][i]
    s=0
    for t in range(u+1):
        if t*(u-t)>v:
            s+=1
    p*=s
print(p)
#part 2: for the actual AOC I did a manual binary search to find the points where you start and stop winning, but here I will show the bruteforce solution as that is good enough with the small input.
#I again hardcoded the input. Assign a and b to the concatenation of the top values and bottom values respectively.
a=60947882
b=475213810151650
s=0
for i in range(0,a,1):
    if i*(a-i)>b:
        s+=1
print(s)
