import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]

        heapq.heapify(gifts)

        for _ in range(k):
            largest = heapq.heappop(gifts)
            square = -math.floor(math.sqrt(abs(largest)))
            heapq.heappush(gifts, square)
        
        return abs(sum(gifts))
        