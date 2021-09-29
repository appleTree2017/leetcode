class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.cache = {}
        
        return self.recursive(stones, 0, 0, 0)
    
    def recursive(self, stones: List[int], index:int, sum_1, sum_2):
        if index == len(stones):
            return abs(sum_1 - sum_2)
        key = str(index) + '#' + str(sum_1)+'#'+ str(sum_2)
        if  key not in self.cache:
            diff_1 = self.recursive(stones, index+1, sum_1 + stones[index], sum_2)
            diff_2 = self.recursive(stones, index+1, sum_1, sum_2 + stones[index])
            self.cache[key] = min(diff_1, diff_2)
        
        return self.cache[key] 
