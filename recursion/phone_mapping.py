def lettercombination (self, digits:str):
    if digits =="":
        return []
    phn_map =  {
        '2':'abc', '3':'def', '4':'ghi','5':'jkl','6':'mno','7':'pqrs' ,'8':'tuv','9':'wxyz'
    }
    result=[]
    def backtrack (index :int, current:str):
        # base case - as ki agar index to unta hi hona chiye jitni length ho unki
        if index == len(digits):
            result.append(current)
            return
        for char in phn_map[digits[index]]:
            backtrack(index+1, current + char)

        

    backtrack(0,"")
    return result