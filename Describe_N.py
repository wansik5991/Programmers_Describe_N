import os
os.system('cls')

from collections import defaultdict

def solution(N, number):
    if N == number : return 1;
    n_lst = defaultdict(set)
    n_lst[1].add(N)
    
    for n_num in range(2, 9) :
        n_lst[n_num].add(int(str(N) * n_num))
        for i in range(1, n_num//2 + 1) :
            for i_num in n_lst[i] :
                for j_num in n_lst[n_num-i] :
                    if 1 <= i_num + j_num <= 32000 : n_lst[n_num].add(i_num + j_num);
                    if 1 <= i_num - j_num <= 32000 : n_lst[n_num].add(i_num - j_num);
                    if 1 <= i_num * j_num <= 32000 : n_lst[n_num].add(i_num * j_num);
                    if 1 <= i_num // j_num <= 32000 : n_lst[n_num].add(i_num // j_num);
                    
                    if 1 <= j_num - i_num <= 32000 : n_lst[n_num].add(j_num - i_num);
                    if 1 <= j_num // i_num <= 32000 : n_lst[n_num].add(j_num // i_num);

                    if number in n_lst[n_num] :
                        return n_num
    return -1


print(solution(2,11),3)
print(solution(5,5),1)
print(solution(5,10),2)
print(solution(5,31168),-1)
print(solution(1,1121),7)
print(solution(5,1010),7)
print(solution(3,4),3)
print(solution(5,5555),4)
print(solution(5,5550),5)
print(solution(5,20),3)
print(solution(5,30),3)
print(solution(6,65),4)
print(solution(5,2),3)
print(solution(5,4),3)
print(solution(1,1),1)
print(solution(1,11),2)
print(solution(1,111),3)
print(solution(1,1111),4)
print(solution(1,11111),5)
print(solution(7,7776),6)
print(solution(7,7784),5)
print(solution(2,22222),5)
print(solution(2,22223),7)
print(solution(2,22224),6)
print(solution(2,11111),6)
print(solution(2,11),3)
print(solution(2,111),4)
print(solution(2,1111),5)
print(solution(9,36),4)
print(solution(9,37),6)
print(solution(9,72),3)
print(solution(3,18),3)
print(solution(2,1),2)
print(solution(4,17),4)
print(solution(5,10))
print(solution(2,11))