def genrtaeParenthesis(self, n):
    result = []
    def doitAGAIN(current: str,open: int,close:int):
        # base case
        # doitAGin is backtrack 
        
        if open ==0 and close ==0:
            result.append(current)
            return
        if open >0:
            doitAGAIN(current + '(', open-1,close)
        if close > open:
            doitAGAIN(current +')',open,close-1)
    doitAGAIN("",n,n)
    return result       


        
