class Solution(object):
    def strStr(haystack, needle):
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i: i+len(needle)] == needle:
                    return i
        return -1


if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"
    print(Solution.strStr(haystack, needle))