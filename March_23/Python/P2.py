#Finding Pairs - tushar pandey

n_iter = int(input())
for i in range(n_iter):     # iterate over test cases
    N = int(input())        # take input for N
                            # take input of array and save in arr
    arr = [int(x) for x in input().split()]
    count = 0               # counter var
    for i, e in enumerate(arr): # iterate over arr, with index and val
        for e1 in arr[i:]:  # iterate over elements ahead from current elemnt
            if e1 == e:     # base condition
                count += 1  # condition true, increase counter
    print(count)            # print answer
