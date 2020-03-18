class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return []
            
        rst = []

        def generate(i, num, ans):
            if len(ans) == 2 * n:
                rst.append(ans)
                return
                
            if i > 0:
                generate(i-1, num, ans+")")
            if num < n:
                generate(i+1, num+1, ans+"(")
            

        generate(0, 0, "")
        return rst
