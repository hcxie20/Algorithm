class Solution:
    def findLadders(self, beginWord,endWord,wordList):
        if endWord not in wordList:
            return []

        word_map = {}

        for word in wordList + [beginWord]:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                if pattern not in word_map:
                    word_map[pattern] = [word]
                else:
                    word_map[pattern].append(word)

        min_length = float('inf')
        queue = [[beginWord, None, 1]]
        history = {}

        rst = []

        while queue:
            item = queue.pop(0)
            word = item[0]
            parent = item[1]
            length = item[2]
            history[word] = parent

            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                for neighbor in word_map[pattern]:
                    if neighbor not in history and neighbor not in queue:
                        queue.append([neighbor, word, length + 1])
                    
                    if neighbor == endWord and length <= min_length:
                        min_length = length
                        one_rst = [word, neighbor]
                        while parent is not None:
                            one_rst.insert(0, parent)
                            parent = history[parent]
                            
                        rst.append(one_rst)
        
        return rst


if __name__ == '__main__':
    begin = "hit"
    end = "cog"
    word_list = ["hot","dot","dog","lot","log","cog"]
    # begin = "a"
    # end = "d"
    # word_list = ["a", "b", "c"]
    # begin = "hot"
    # end = "dog"
    # word_list = ["hot", "dog"]
    print(Solution().findLadders(begin, end, word_list))
