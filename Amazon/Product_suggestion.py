class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        res = []
        for i in range(1, len(searchWord) + 1):
            chars = searchWord[:i]
            tmp = []
            for product in products:
                if product[:i] == chars:
                    if len(tmp) < 3:
                        tmp.append(product)
                    else:
                        break
            res.append(tmp)
            
        return res