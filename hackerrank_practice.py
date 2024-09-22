class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int 
        :rtype: bool 
        """
        count = 0  # Count of flowers we can plant
        i = 0  # Pointer to traverse the flowerbed
        
        while i < len(flowerbed):
            # Check if the current spot is empty and the adjacent spots are also empty or out of bounds
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1  # Plant a flower
                count += 1  # Increment the count of flowers planted
            
            i += 1  # Move to the next spot
        
        return count >= n  # Check if we can plant at least n flowers

# Example usage
if __name__ == '__main__':
    solution = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    result = solution.canPlaceFlowers(flowerbed, n)
    print(result)  # Output: True

    n = 2
    result = solution.canPlaceFlowers(flowerbed, n)
    print(result)  # Output: False
