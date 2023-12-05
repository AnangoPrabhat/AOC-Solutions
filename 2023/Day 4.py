#for both parts: s is the input, as a string

su=0
co=0
ct2=0
o=1
z=11

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

s=intspace(s.split('\n'))


#part 1
def solve(i):
    
    S=list(i[1:z])
    ct=list(i[z:])
    tau=0
    for i in ct:
        tau+=S.count(i)
    return tau
print(sum(int(2**(solve(i)-1)//1) for i in s))

#part 2

dp=[0 for _ in range(len(s))]

dp[0]=1
dp[1]=1
for i in range(123739831823781233237898217323):
    if i<len(dp):
        dp[i]=o
    else:
        break
m=0

for i in range(0,len(s)):
    t=solve(s[i])
    for j in range(i+1,i+t+1):
        dp[j]+=dp[i]
    #print(i,t,dp[t])
    
        
    
    
print(sum(dp))
