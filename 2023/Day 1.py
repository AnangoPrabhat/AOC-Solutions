#part 1 - s input as a string

print(sum(map(int,[(x:=list(filter(lambda y:y.isdigit(),i)))[0]+x[-1] for i in s.split('\n')])))

#part 2 - s input as a string

def all2(s):
    l=[]
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            l.append(s[i:j])
    return l
def all3(s):
    
    return all2(s[::-1])
  
ct=0
ndict={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
for i in s.split('\n'):
    #t is the splitted result of each line
    for j in all2(i):
        if j in ndict or j in '123456789':
            first=(int(j) if j in '123456789' else ndict[j])
            break
    for j in all3(i):
        if j[::-1] in ndict or j in '123456789':
            last=(int(j) if j in '123456789' else ndict[j[::-1]])
            break
            
    if 1:
        ct+=int(str(str(first)+str(last)))
    
print(ct)
