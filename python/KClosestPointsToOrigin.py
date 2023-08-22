class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distances = [(math.sqrt(x*x + y*y), i) for i, (x, y) in enumerate(points)]
    
        sorted_distances = sorted(distances)
    
        return [points[i] for d, i in sorted_distances[:k]]
            
        
