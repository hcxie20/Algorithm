class Tire:
    def __init__(self):
        self.root = TireNode()

    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            ch = word[i]
            if not node.has_value(ch):
                node.put(ch)
            node = node.get(ch)
        node.set_end()

    def search_prefix(self, word):
        node = self.root
        for i in range(len(word)):
            ch = word[i]
            if node.has_value(ch):
                node = node.get(ch)
            else:
                return None
        return node

    def search(self, word):
        node = self.search_prefix(word)
        return node != None and node.is_end()
    
    def search_with(self, prefix):
        node = self.search_prefix(prefix)
        return node != None
        

class TireNode:
    def __init__(self):
        self.r = 26
        self.links = [None] * self.r
        self.isEnd = False

    def has_value(self, ch):
        return self.links[ord(ch) - ord("a")] != None

    def get(self, ch):
        return self.links[ord(ch) - ord("a")]
    
    def put(self, ch):
        self.links[ord(ch) - ord("a")] = TireNode()

    def set_end(self):
        self.isEnd = True

    def is_end(self):
        return self.isEnd


if __name__ == "__main__":
    a = Tire()
    a.insert("eat")
    a.insert("eaa")
    a.insert("eas")
    a.insert("ead")
    a.insert("ear")
    a.insert("e")
    a.insert("eay")
    # a.insert("ae")
    # a.insert("aesdf")
    print(a.search("ea"))
    print(a.search_with("ea"))
    print(a.search("s"))
    print(a.root.links.count(None))
    pass
