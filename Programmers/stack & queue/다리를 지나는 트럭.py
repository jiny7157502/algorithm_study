from collections import deque

def solution(bridge_length, bridge_weight, truck_weights):
    list = [0 for i in range(bridge_length)]

    deq = deque(list)
    truck_deq = deque(truck_weights)

    result = 0
    weight = 0
    while deq:
        result += 1
        weight -= deq.popleft()
        
        if truck_deq:
            if weight + truck_deq[0] <= bridge_weight:
                truck = truck_deq.popleft()
                deq.append(truck)
                weight += truck
            else:
                deq.append(0)
    
    return result

print(solution(2, 10, [7,4,5,6])) # 8
print(solution(100, 100, [10])) # 101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10])) # 110