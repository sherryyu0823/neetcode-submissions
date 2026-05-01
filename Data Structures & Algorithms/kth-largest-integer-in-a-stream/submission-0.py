class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

        heapq.heapify(self.arr)

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        k = self.k
        l = len(self.arr)
        while k < len(self.arr):
            heapq.heappop(self.arr)
        return self.arr[0]
        
