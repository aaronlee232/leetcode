class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def getSum(num: int) -> int:
            sum = 0
            while num != 0:
                sum += num % 10
                num //= 10
            return sum
        
        boxes = [0] * 46
        maxId = 0;
        for num in range(lowLimit, highLimit + 1):
            boxId = getSum(num)
            boxes[boxId] += 1
            if boxes[boxId] > boxes[maxId]:
                maxId = boxId
        return boxes[maxId]
        