present_cup = [1,2,3]

M = int(input())

if (1<=M<=50):
    for i in range(M):
        x, y = map(int, input().split())
        a = present_cup.index(x)
        b = present_cup.index(y)

        tmp = present_cup[a]
        present_cup[a] = present_cup[b]
        present_cup[b] = tmp

    print(present_cup[0])
            
'''
m = int(input())

cup = [0, 1, 0, 0]  ## cup[1]에 공이 있음

for i in range(m) :
    a,b = list(map(int, input().split()))
    cup[a], cup[b] = cup[b], cup[a]

if cup[1] == 1 :
    print(1)
elif cup[2] == 1 :
    print(2)
else :
    print(3)
'''