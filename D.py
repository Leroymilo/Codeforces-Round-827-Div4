def gcd(a, b) :
    if a * b == 0 :
        return 0
    a, b = max(a, b), min(a, b)
    if a == b :
        return a
    return gcd(a-b, b)

for _ in range(int(input())) :
    n = int(input())
    A = list(map(int, input().split()))

    found = set()
    I = []
    for i in range(n-1, -1, -1) :
        if A[i] not in found :
            found.add(A[i])
            I.append(i)
        if len(found) == 1000 :
            break
    
    best = (-1, -1)
    for i in range(len(I)) :
        if 2 * I[i] <= sum(best) :
            break
        for j in range(i, len(I)) :
            if I[i] + I[j] <= sum(best) :
                break

            elif gcd(A[I[i]], A[I[j]]) == 1 :
                best = (I[i], I[j])
    
    if best == (-1, -1) :
        print(-1)
    
    else :
        print(sum(best) + 2)