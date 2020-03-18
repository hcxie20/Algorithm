class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tmp = self.root
        for i in range(len(word)):
            if word[i] not in tmp.nodes:
                tmp.nodes[word[i]] = TreeNode()
            tmp = tmp.nodes[word[i]]
            if i == len(word) - 1:
                tmp.isKey = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp = self.root
        for i in range(len(word)):
            if word[i] not in tmp.nodes:
                return False
            tmp = tmp.nodes[word[i]]
            if i == len(word) - 1 and not tmp.isKey:
                return False
        return True


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp = self.root
        for i in range(len(prefix)):
            if prefix[i] not in tmp.nodes:
                return False
            tmp = tmp.nodes[prefix[i]]
        return True

class TreeNode:
    def __init__(self):
        self.isKey = False
        self.nodes = {}