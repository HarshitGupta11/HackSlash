#Finding Pairs - tushar pandey

n_iter = int(input())
for i in range(n_iter):
    N = int(input())
    arr = [int(x) for x in input().split()]
    count = 0
    for i, e in enumerate(arr):
        for e1 in arr[i:]:
            if e1 == e:
                count += 1
    print(count)
