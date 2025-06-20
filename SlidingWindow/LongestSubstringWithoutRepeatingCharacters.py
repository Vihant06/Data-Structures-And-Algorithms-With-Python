def lengthOfLongestSubstring(self, s):

    sett = set()
    l = 0
    longest = 0
    n = len(s)

    for r in range(n):

        while s[r] in sett:

            sett.remove(s[r])
            l += 1

        w = (r - l) + 1
        longest = max(longest, w)

    return longest
# Time complexity: O(n)
# Space complexity: O(1)
