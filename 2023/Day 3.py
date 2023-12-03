#both parts: s is the string input
from collections import *

def ip(sc, row, col):
    pos = [(i,j) for i in range(-1,2) for j in range(-1,2)]
    pos.remove((0,0))

    for dx, dy in pos:
        ni, nj = row + dx, col + dy
        if 0 <= ni < len(sc) and 0 <= nj < len(sc[0]) and sc[ni][nj] != '.' and sc[ni][nj] not in "0123456789":
            return True

    return False
def ap(sc, row, col):
    pos = [(i,j) for i in range(-1,2) for j in range(-1,2)]
    pos.remove((0,0))

    p = []

    for dx, dy in pos:
        ni, nj = row + dx, col + dy
        if 0 <= ni < len(sc) and 0 <= nj < len(sc[ni]) and sc[ni][nj] in "0123456789":

            p.append(dp[(ni,nj)])
            

    return list(set(p)) #hope for no duplicates!

# Sample input
sc= s.split('\n')

dp=defaultdict(lambda:0)
su = 0
S=set()
dp = {}
t=0
for i in range(len(sc)):
    t=0
    for j in range(len(sc[i])):
        if j<t:
            continue
        tau=''
        gg=0
        for t in range(j,len(sc[i])):

            if sc[i][t] in "0123456789":
                tau+=sc[i][t]
            else:
                break
            if ip(sc, i, t):
                gg=1
        if tau=='':
            continue
        u=int(tau)
        for t in range(j,len(sc[i])):

            if sc[i][t] in "0123456789":
                tau+=sc[i][t]
            else:
                break
            if ip(sc, i, t):
                gg=1
            dp[(i,t)]=u
        if gg:
            su += u
            #print(u)
gs = 0
for i in range(len(sc)):
    for j in range(len(sc[i])):
        if sc[i][j] == '*':
            p8= ap(sc, i, j)
            if len(p8) == 2:
                gs += p8[0]*p8[1]

print("Part 1:", su)
print("Part 2:", gs)
 
