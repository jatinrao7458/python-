def combinationSum(self, candidates:list[int], target: int):
    result = []
    # start = index
    # current as candidates
    def backtreck (start:int,current :list[int],total:int):
        if target == total:
            result.append(list(current))
        if total>target:
            return
        for i in range (start, len(candidates) ):
            current.append(candidates[i])
            backtreck(i,current,total +candidates[i])
            current.pop()

    backtreck(0,[],0)
    return result