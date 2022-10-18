for _ in range(int(input())) :
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    K = list(map(int, input().split()))

    M, H = [A[0]], [A[0]]
    biggest = A[0]
    for i in range(1, n) :
        biggest = max(biggest, A[i])
        M.append(biggest)
        H.append(H[-1] + A[i])

    res = []
    for k in K :
        if M[0] > k :
            res.append(0)
            continue
        
        b, h = 0, n-1
        while b < h :
            m = (h + b) // 2
            if M[m] > k :
                h = m - 1
            elif M[m] <= k :
                b = m + 1

        if M[b] > k :
            res.append(H[b-1])
        else :
            res.append(H[b])
    
    print(*res)