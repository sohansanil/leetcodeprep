class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            left = 0 if i==0 else flowerbed[i-1]
            right = 0 if i == len(flowerbed)-1 else flowerbed[i+1]
            current = flowerbed[i]
            if left == 0 and current == 0 and right == 0:
                flowerbed[i] =1
                n-=1
                if n<=0:
                    return True
                   
        return n <= 0
                

        