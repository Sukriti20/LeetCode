class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hammingDistance=0
        while x>0 or y>0:
            if(x%2 != y%2):
                hammingDistance +=1
            x=x//2
            y=y//2
            
        print(hammingDistance)
        return hammingDistance
