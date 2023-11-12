import random
import time

def naive_search(l , target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


def binary_search( l , target , low = None , high = None):
    if low is None:
        low = 0
    if high is None :
        high = len(l) - 1
    
    # just to test
    print('test')

    mid_point = (low + high) // 2
    
    if l[mid_point] == target:
        return mid_point
    elif target < l[mid_point]:
        return binary_search(l , target , low  , mid_point - 1)
    else:
        return binary_search(l , target , mid_point + 1 , high)
    
if __name__ == '__main__':
    # l = [1 , 3 , 5, 10 , 12]
    # target = 10
    # print(naive_search(l , target))
    # print(binary_search(l , target))
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length , 3 * length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()

    for target in sorted_list:
        binary_search(sorted_list , target)
    end = time.time()

    print(f'search time in binary is ', (end - start) / length )

    
