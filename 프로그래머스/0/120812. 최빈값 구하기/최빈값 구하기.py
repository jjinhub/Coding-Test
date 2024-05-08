from collections import Counter

def solution(array):
    sH = Counter(array)
    sH_max = max(sH.values())
    
    max_list = []
    for num, cnt in sH.items():
        if cnt == sH_max:
            max_list.append(num)
            
    if len(max_list) > 1:
        return -1

    return max_list[0]