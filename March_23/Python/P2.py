#Finding Pairs

def print_op():
    n=int(input())
    temp=input()
    c=0
    arr=[int(x) for x in temp.split()]
    for i in range(n):
        for j in range(i,n):
            if arr[i]==arr[j]:
                c+=1
    print(c)


def main():
    n=int(input())
    for j in range(n):
        print_op()

main()
