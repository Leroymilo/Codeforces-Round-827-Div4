for _ in range(int(input())) :
    input()
    grid = [input() for _ in range(8)]

    for i in range(8) :
        if grid[i] == 'R'*8 :
            print('R')
            break
    else :
        print('B')