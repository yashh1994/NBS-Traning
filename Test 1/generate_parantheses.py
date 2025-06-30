def generateParenthesis(self, n: int) -> List[str]:
        def go(cur,li,open):
            if len(cur) > 2*n:
                return
            if len(cur) == 2*n and open == 0:
                li.append(cur)
                return 
            if open+1 <= n and len(cur)<2*n:
                go(cur+"(",li,open+1)
            if open:
                go(cur+")",li,open-1)
        li = []
        go("",li,0)
        return li