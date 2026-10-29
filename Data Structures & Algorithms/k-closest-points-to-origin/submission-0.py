class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       
       
        def distance(coord) -> int:
            x1, y1 = coord
            return (math.sqrt((x1)**2 + (y1)**2))

        arr = []
        heapq.heapify(arr)

        for pt in points:
            dist = distance(pt)
            heapq.heappush(arr, (dist, pt))

        answer = []

        for i in range(k):
            dist, pt = heapq.heappop(arr)
            answer.append(pt)

        return answer