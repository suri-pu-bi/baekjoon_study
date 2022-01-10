'''"나는 요리사다"는 다섯 참가자들이 서로의 요리 실력을 뽐내는 티비 프로이다. 
각 참가자는 자신있는 음식을 하나씩 만들어오고, 서로 다른 사람의 음식을 점수로 평가해준다. 
점수는 1점부터 5점까지 있다.

각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합이다. 
이 쇼의 우승자는 가장 많은 점수를 얻은 사람이 된다.

각 참가자가 얻은 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램을 작성하시오.
총 다섯 개 줄에 각 참가자가 얻은 네 개의 평가 점수가 공백으로 구분되어 주어진다. 
첫 번째 참가자부터 다섯 번째 참가자까지 순서대로 주어진다. 
항상 우승자가 유일한 경우만 입력으로 주어진다.'''

# for문 첫 번째 참가자부터 다섯번째 참가자까지 1점 ~ 5점

from random import *

def sort (s_list) :
    s_list.sort()
    print(s_list)
    print(s_list[4])
    return s_list[4]

score_list = []


for i in range(1,6):
    f_score = 0
    for j in range(1,5) :
        score = int(input().split)
        if 1<=score<=5 :
            f_score += score
            print(score,end=" ")
         
    
    score_list.append(f_score)    
    print()

print(score_list)
final_score = sort(score_list)
print(score_list)
winner = score_list.index(final_score)
print(winner+1, final_score)

