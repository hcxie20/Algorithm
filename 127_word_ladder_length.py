class Solution:
    def ladderLength(self, beginWord,endWord,wordList):
        if endWord not in wordList:
            return 0

        word_map = {}

        for word in wordList + [beginWord]:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                if pattern not in word_map:
                    word_map[pattern] = [word]
                else:
                    word_map[pattern].append(word)

        queue = [[beginWord, 1]]
        history = set()

        while queue:
            item = queue.pop(0)
            word = item[0]
            length = item[1]
            history.add(word)

            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                for neighbor in word_map[pattern]:
                    if neighbor not in history and neighbor not in queue:
                        queue.append([neighbor, length + 1])
                    
                    if neighbor == endWord:
                        return length + 1
        
        return 0


from typing import List
from collections import deque


class SolutionT:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)

        queue = deque()
        queue.append(beginWord)

        visited = set(beginWord)
        visited.add(beginWord)

        word_len = len(beginWord)
        step = 1
        while queue:
            current_size = len(queue)
            for i in range(current_size):
                word = queue.popleft()

                word_list = list(word)
                for j in range(word_len):
                    origin_char = word_list[j]

                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                visited.add(next_word)
                    word_list[j] = origin_char
            step += 1
        return 0


if __name__ == '__main__':
    # begin = "hit"
    # end = "cog"
    # word_list = ["hot","dot","dog","lot","log","cog"]
    # begin = "a"
    # end = "d"
    # word_list = ["a", "b", "c"]
    begin = "hot"
    end = "dog"
    word_list = ["hot", "dog"]
    print(Solution().ladderLength(begin, end, word_list))
