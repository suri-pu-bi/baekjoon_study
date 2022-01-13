'''
거스름돈의 액수가 주어지면 리암이 줘야할 쿼터(Quarter, $0.25)의 개수, 
다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수를 
구하는 프로그램을 작성하시오. 
거스름돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 하려고 한다. 
예를 들어, $1.24를 거슬러 주어야 한다면, 손님은 4쿼터, 2다임, 0니켈, 4페니를 받게 된다.
'''
Quarter = 25
Dime = 10
Nickel = 5
Penny = 1 

testcase_list = []

T = int(input())
for i in range(0,T) :
    testcase = int(input())
    if testcase <= 500 :
        testcase_list.append(testcase)


for i in range(T) :
    num_q = testcase_list[i]// Quarter
    num_d = testcase_list[i]% Quarter // Dime
    num_n = testcase_list[i]% Quarter % Dime // Nickel
    num_p = testcase_list[i]% Quarter % Dime % Nickel // Penny
    print(num_q, num_d, num_n, num_p, end=" ")
    print()