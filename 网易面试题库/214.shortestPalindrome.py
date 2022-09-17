"""
回文经常考虑将字符串反转
"""



class Solution():
    def shortestPalindrome( s: str) -> str:
        rev_s = s[::-1]
        for i in range(len(s)):
            if s.startswith(rev_s[i:]):
                return rev_s[:i] + s

    def  shortestPalindrome_v2( s: str) -> str:

        """
        kmp模板
        """
        def kmp(s):
            next = [0] * (len(s)+1)
            i, j = 1, 0
            while i <len(s):
                if j==0 or s[i] == s[j]:
                    i += 1
                    j += 1
                    next[i] = j
                else : 
                    j = next[j]
            #next[j]的含义是：在子串的第j个字符与主串发生失配时，则跳到子串的next[j]位置重新与主串当前位置进行比较
            return next
        pi = kmp(s + '#' + s[::-1])
        print(s + '#' + s[::-1])
        print(pi)
        if pi[-1] == len(s):
            return s 
        else:
            print(s[pi[-1]:])
            return s[pi[-1]:][::-1] + s    





if __name__=="__main__":
    s = "aacecaaa"
    print(Solution.shortestPalindrome(s))
    print(Solution.shortestPalindrome_v2(s))