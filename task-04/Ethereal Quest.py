n = int(input())

if 1 <= n <= 100:
    sumx = 0
    sumy = 0
    sumz = 0
    
    for _ in range(n):
        x, y, z = map(int, input().split())
        
        if -100 <= x <= 100 and -100 <= y <= 100 and -100 <= z <= 100:
            sumx += x
            sumy += y
            sumz += z
        else:
            print("Invalid coordinates.")
            break
        
    if sumx == 0 and sumy == 0 and sumz == 0:
        print("YES")
    else:
        print("NO")
else:
    print("Invalid number of force vectors.")
