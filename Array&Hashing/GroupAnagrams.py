from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            anagrams_dict[tuple(count)].append(s)

        return list(anagrams_dict.values())


# Time complexity: O(N * K)
# Space Complexity: O(N * K)
