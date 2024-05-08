def solution(array):
    answer = 0
    array.sort()
    center_index = len(array) // 2
    answer = array[center_index]
    return answer