class Solution:
    def __init__(self):
        self.result= []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        self.helper(sorted(candidates), target,target, 0, [])
        return self.result
        
    def helper(self, candidates, target,origTarget, index, path):
        # base 
        if target < 0 or candidates[index]>origTarget: return
        if target == 0:
            self.result.append(path[:])
            return
        
        # logic
        # if we set range here to start from 0, we get all permutations, else
        # set it to start from `index` and we get all combinations
        for i in range(index,len(candidates)):
            path.append(candidates[i])
            self.helper(candidates, target-candidates[i], origTarget, i, path)
            path.pop()

