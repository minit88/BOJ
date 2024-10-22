"""
출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고 이 막대들 사이에 가로 방향의
선들이 또한 랜덤하게 연결된다.
X=0인 출발점에서 출발하는 사례에 대해 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동가능한
"""
from collections import deque
from copy import deepcopy
import sys
sys.stdin = open('input.txt', 'r')

for i in range(10):
    test_case = int(input())

    """
    입력 받기
    """
    array = []
    for _ in range(100):
        array.append(list(map(int,input().split())))

    """
    x 0부터 99까지 출발
    """

    for start_x in range(100):
        q= deque([])
        q.append((1,start_x)) # y,x

        visited_list = deepcopy(array)
        while q:
            current_y, current_x = q.popleft()

            if visited_list[current_y][current_x] == 1:
                visited_list[current_y][current_x] = 0 # 방문 처리
            else:
                continue

            for d_y, d_x in [(0,-1),([0,1]),(1,0)]:
                next_y = current_y + d_y
                next_x = current_x + d_x

                if 0<= next_y<100 and 0<= next_x<100:
                    if visited_list[next_y][next_x] == 1:
                        q.append((next_y,next_x))
                        break
                    elif visited_list[next_y][next_x] == 2:
                        print("#%d %d" %(test_case,start_x))

                        q.clear()
                        break



