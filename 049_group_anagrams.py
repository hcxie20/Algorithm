import collections

class Solution:
    def groupAnagrams(self, strs):
        dict = collections.defaultdict(list)

        for s in strs:
            tmp = [0] * 26
            for c in s:
                tmp[ord(c) - ord("a")] += 1
            dict[tuple(tmp)].append(s)

        return list(dict.values())