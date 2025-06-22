def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq_s = {}
    freq_t = {}

    for c in s:
        freq_s[c] = freq_s.get(c, 0) + 1
    for c in t:
        freq_t[c] = freq_t.get(c, 0) + 1
    return freq_s == freq_t
# Time complexity: O(n + m)
# Space complexity: O(1)
