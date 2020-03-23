#When the Sepratist Next Attack
"""
Two basic insights are:
1.The base is gonna be the number of unique characters in the code since it will be the only one that would generate the 
least number.
2. The first charcater in the code will always be coded as 1 and the second unique character as 0 to get the lowest 
numeric representation.
"""

def get_score():
    code=input()
    c=2
    #indicator used to map the first and the secod character.
    flag=0
    #dictionary/map for the characters to store the mapping from characters to the value.
    code_dict={}
    for j in range(len(code)):
        try:
            _=code_dict[code[j]]
        except:
            if flag==0:
                #map the first character as 1
                code_dict[code[j]]=1
                flag+=1
            elif flag==1:
                #map the second character as 0
                code_dict[code[j]]=0
                flag+=1
            else:
                #map rest of them on the values of c
                code_dict[code[j]]=c
                c+=1
    #base will be the number of unique characters in the code. Since the base cannot be unary we taking the max b/w 2 and no. of chars.
    base=max(len(code_dict),2)
    secs=0
    c=0
    #iterate in the reverse order of code. Normal conversion of code to numeric representation and then conversion to base 10.
    for j in range(len(code)-1,-1,-1):
        #raise the base to the position and multiply with numneric value
        secs+=((base**c)*code_dict[code[j]])
        c+=1
    #print the results
    print(secs)
    
def main():
    n=int(input())
    for i in range(n):
        get_score()

main()