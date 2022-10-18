for _ in range(int(input())) :
    n = int(input())
    l = list(map(int, input().split()))

    if len(l) == len(set(l)) :
        print("YES")
    else :
        print("NO")