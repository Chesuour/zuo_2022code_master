class Solution:
    def lengthOfLongestSubstring( s: str) -> int:
        if not s : return 0
        subs = set()
        max_len, cur_len = 0, 0
        left = 0
        for i in range(len(s)):
            cur_len += 1
            while s[i] in subs:
                subs.remove(s[left])
                left += 1
                cur_len -= 1
            max_len = cur_len if cur_len > max_len else max_len
            subs.add(s[i])
        return max_len

if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution.lengthOfLongestSubstring(s))



