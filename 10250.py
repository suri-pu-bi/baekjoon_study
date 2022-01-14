T = int(input())
room = []
for i in range(T):
    testcase_list = list(map(int, input().split()))
    H, W, N = testcase_list[:]

    if (1<=H) & (W<=99) & (1<=N<=H*W) :
        
        if (H<=N) :
            if (N%H==0) :
                room_w = N//H
                room_h = H
            else :
                room_w = N//H + 1
                room_h = N%H

        else:
            room_w = 1
            room_h = N
    
        room.append(room_h)
        room.append(room_w)
    
for j in range(0,len(room),2):
    if (room[j+1]<10):
        print(room[j], room[j+1], sep="0")
    else :
        print(room[j], room[j+1], sep="")

# 12012가 될 수 있으므로 오류 발생
# 99 99 1 오류발생