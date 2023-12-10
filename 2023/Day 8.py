from collections import *
from sympy.ntheory.modular import crt







#replace s2 with the input, and s is the graph input
s2 = 'LRRRLRRLRLLRLRRLRLRLLRRRLRLRRRLRRRLRLRLRRLRLRRRLRRLLRRLLLRRLRRLRRRLRLRRRLRRLRRRLRRRLRRLRLLRRRLRLRRLRLRLRRRLRRLLRRRLLRRLRLRRLRRRLLLRRRLLRLLRRLRRRLRLRLRRLLLRRRLLRRLLLRLRLRRLLRLLRRLLLRRLLRRRLRLRRRLRLLRRRLRRRLRLRLRRRLRLRRRLRRRLRRRLLRLRLRLRRLRLRRRLRLRLLRRLRRLRRLRRRLRRRLRLLRLLLRRLRLRRRR'
G = {}
lines = s.split('\n')

for line in lines:
    x,y = line.split(' = ')
    node = x
    a,b = y.split(', ')
    a=a[1:]
    b=b[:-1]
    G[node] = (a,b)

m=0
l2=[]
for i in G:
    if i[-1]=='A':
        l2.append(i)
cn=l2[:]
cn3=l2[:]
ct = 0
bools=[]
cn=[]
dp=defaultdict(lambda:[])
visited = l2[:]
while ct<10**5:
    for tau in s2:
        ct += 1
        cn=[]
        for i,cn2 in enumerate(cn3):
            nn = (G[cn2][1] if tau == 'R' else G[cn2][0])
            cn2 = nn

            cn.append(nn)
            if nn[-1]=='Z':
                dp[i].append(ct)
        visited=cn[:]
        cn3=cn[:]
    
from sympy.ntheory.modular import crt

v1=[]
v2=[]
for i in dp:
    v1.append((1+dp[i][0])%(dp[i][1]-dp[i][0]))
    v2.append(dp[i][1]-dp[i][0])
ct=0
cur='AAA'
ct2=0
ct=0
while cur!='ZZZ':
    cur = (G[cur][0] if s2[ct2]=='L' else G[cur][1])
    ct2+=1
    ct+=1
    ct2%=len(s2)
print(ct,crt(v2,v1)[1])
