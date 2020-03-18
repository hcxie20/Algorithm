class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        rst = []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def find(cur, combo):
            for letter in letters[digits[cur]]:
                if cur == len(digits) - 1:
                    rst.append(combo + letter)
                else:
                    find(cur+1, combo + letter)
        
        find(0, "")
        return rst
