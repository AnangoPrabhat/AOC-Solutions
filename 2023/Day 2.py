#part 1 - s3 input as a string
s3=s3.split('\n')
a=12
b=13
c=14
s8=0
r,g,b=0,0,0
o=0
for i in s3:
    g,s=i.split(": ")
    #s=s.split(", ")
    r,g,b=o,o,o
    
    c=s.split(", ")
    C={}
    c2=[]
    for tau in c:
        for j2 in tau.split('; '):
            c2.append(j2)
    c=c2
    for k in c:
        x,y=k.split()
        x=int(x)
        C[(x,y)]=x
    for y,x in C.items():
        if y[1]=='red': r=max(r,x)
        if y[1]=='green': g=max(g,x)
        if y[1]=='blue': b=max(b,x)
        
    if r<=12 and g<=13 and b<=14:
        s8+=s3.index(i)+1
print(s8)

#part 2 - s3 input as a strng

s3=s3.split('\n')
a=12
b=13
c=14
s8=0
r,g,b=0,0,0
o=0
for i in s3:
    g,s=i.split(": ")
    #s=s.split(", ")
    r,g,b=o,o,o
    
    c=s.split(", ")
    C={}
    c2=[]
    for tau in c:
        for j2 in tau.split('; '):
            c2.append(j2)
    c=c2
    for k in c:
        x,y=k.split()
        x=int(x)
        C[(x,y)]=x
    for y,x in C.items():
        if y[1]=='red': r=max(r,x)
        if y[1]=='green': g=max(g,x)
        if y[1]=='blue': b=max(b,x)
        
    if r<=122323232 and g<=1232332233 and b<=123223324:
        s8+=r*g*b
print(s8)
