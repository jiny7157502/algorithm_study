import heapq

heap = []

# heapq.heappush() : 힙에 원소 추가하는 메소드
# heapq.heappush(원소를 추가할 대상 리스트, 추가할 원소)
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap) # [1, 3, 7, 4]

# heapq.heappop() : 힙에서 원소 삭제
# 가장 작은 값 삭제 후 삭제된 값 리턴
print(heapq.heappop(heap))
print(heap)

# heap[0] : 힙의 최소값 구하기(삭제 x)
print(heap[0])

# heapq.heapify(heap) : 리스트를 힙으로 변환
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)