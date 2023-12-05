#part 1. s is the input: make sure to include a newline for both parts before the string input.
def stripall(text,rule):
    '''strip all chars in text not in rule'''
    return ''.join(i for i in text if i in rule)
def intspace(textlist):
    digits="0123456789"
    l=[]
    for i in textlist:
        s=''
        for j in i:
            if j not in digits:
                s+=" "
            else:
                s+=str(j)
        l.append(list(map(int,stripall(s,digits+" ").split())))
        
    return l

cur=set()

s=[intspace(i.split('\n'))[1:] for i in s.split('\n\n')]
s[-1]=s[-1][:-1]
S=set()
counter=0
sc=s[0]
S=set(sc[0])
visited1=set()
for i in s[1:]:
    m={}
    for tau in S:
        for j in i:
            a,b,c=j
            if b<=tau<b+c:
                m[tau]=a+tau-b
        if tau not in m:
            m[tau]=tau
    visited1=set(m.values())
    S=visited1
print(min(S))


#part 2. Manually binary search on the value of n around the approximation returned by the first section of the program, checking whether 'success' is seen. The answer
#is the smallest n such that SUCCESS is seen. 
cur=set()

s=[intspace(i.split('\n'))[1:] for i in s.split('\n\n')]#[:-1]
s[-1]=s[-1][:-1]
S=set()
counter=0
sc=s[0]
T=sc[0]
S=set()
M=1000
def rnd(n):
    return int(f'{float(f"{n:.5g}"):g}') #rounded n to k sf
for i in range(len(T)//2):
    for j in range(T[2*i],T[2*i]+T[2*i+1],M):
        if 1:
            S.add(j)
    #print(i,len(T)//2)
print(len(S))
visited1=set()
#S={56}
for i in s[1:]:
    m={}
    for tau in S:
        for j in i:
            a,b,c=j
            if b<=tau<b+c:
                m[tau]=a+tau-b
        if tau not in m:
            m[tau]=tau
    visited1=set(m.values())
    S=visited1
    print(i,len(S))
print(len(S),min(S))
from copy import *
m=46294175
ms=set([m])
n=m
for i in s[::-1][:-1]:
    p=set()
    ms2=deepcopy(ms)
    for r in ms:
        gg=0
        for j in i:
            a,b,c=j
            prev=b-a+r
            #print(i,j,prev)
            if b<=prev<b+c:
                p.add((tuple(j),prev))
                gg=1
        if gg:
            ms2.remove(r)
    #print(p)
    for j in p:
        #print(j)
        ms2.add(j[1])
    #print(ms,ms2,p)
    print(len(ms),len(p))
    ms=deepcopy(ms2)
for i in range(len(T)//2):
    for j in ms:
        if j in range(T[2*i],T[2*i]+T[2*i+1]):
            print('SUCCESS',T[2*i],j,T[2*i]+T[2*i+1])
