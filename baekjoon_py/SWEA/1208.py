"""
높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.
평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1이내가 된다
평탄화 작업을 위해서 상자를 옮기는 작업횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환
"""

T = 10
for test_case in range(1,T+1):
    dump_cnt_lmt = int(input())
    box_height_list = list(map(int,input().split()))

    def find_min_height_and_index():
        min_height = float('inf')
        min_height_idx = 0
        for box_idx in range(len(box_height_list)):
            if min_height>box_height_list[box_idx]:
                min_height = box_height_list[box_idx]
                min_height_idx = box_idx
        return min_height, min_height_idx

    def find_max_height_and_index():
        max_height = float('-inf')
        max_height_idx = 0
        for box_idx in range(len(box_height_list)):
            if max_height<box_height_list[box_idx]:
                max_height = box_height_list[box_idx]
                max_height_idx = box_idx
        return max_height, max_height_idx

    for try_cnt in range(dump_cnt_lmt):
        min_height, min_height_idx = find_min_height_and_index()
        max_height, max_height_idx = find_max_height_and_index()

        box_height_list[min_height_idx]+=1
        box_height_list[max_height_idx]-=1
    result = max(box_height_list) - min(box_height_list)
    print("#%d %d" %(test_case,result))




