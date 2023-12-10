#p1: s is the input
def f(l):
    return (0 if all(i==0 for i in l) else l[-1]+f([l[i+1]-l[i] for i in range(len(l)-1)]))
        

su=0
for i in (s.split('\n')):
    su+=f(list(map(int,i.split())))
print(su)

#p2: s is the input
def f(l):
    return (0 if all(i==0 for i in l) else l[0]-f([l[i+1]-l[i] for i in range(len(l)-1)]))
        

su=0
for i in (s.split('\n')):
    su+=f(list(map(int,i.split())))
print(su)

#This was the biggest jam of the entire AOC for me. I had the function working very quickly, but got stuck in bugs as I was using a prebuilt function to read the integers, which failed to read the negative numbers as negative.  
