#What's the sepratist planning

def get_pats(pat_dict,spc):
    pattern=input()
    pat_split=[]
    flag=0
    temp=[]
    ts=""
    for ch in pattern:
        if ch=="(":
            if len(temp)!=0:
                pat_split.append(temp)
            elif ts!="":
                pat_split.append([ts])
                ts=""
            flag+=1
            continue
        if ch==")":
            pat_split.append(temp)
            temp=[]
            flag=0
            continue
        if flag!=0:
            temp.append(ch)
        else:
            pat_split.append([ch])
    c=0
    count=0
    temp=0
    flag=0
    for key in pat_dict.keys():
        flag=0
        c=0
        for ch in key:
            if ch not in pat_split[c]:
                flag+=1
                break
            c+=1
        if flag==0:
            count+=1
    print(count)
            
    
def main():
    l,d,n=map(int,input().split())
    pat_dict={}
    for i in range(d):
        temp=input()
        pat_dict[temp]=1
    ltemp=[]
    for key in pat_dict.keys():
        for char in key:
            ltemp.append(char)
    spc=list(set(ltemp))
    for i in range(n):
        get_pats(pat_dict,spc)

main()