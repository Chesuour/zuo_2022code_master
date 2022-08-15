"""
Data : 2022/8/15
Author : SuquanChen
Address: 出门问问 苏州

找出字符串中 字符不同子字符串的最大长度

解题思路
1)计算第i个位置的字符前面有多少个不同的字符 一直往前走，直到遇到和他一样的字符
2)再看i-1位置的往左推的长度
选择1)和2)的最短的
"""

class Solution():
    def LengthOfLagestSubstring(string):
        if not string or string == '':
            return 0
        map = {}
        for i in range(len(string)):
            map[string[i]] = -1
        print(map)
        ans = 1
        pre = 1
        for j in range(1,len(string)):
            # p1 = j - map[string[j]]
            # p2 = pre + 1
            # print(p1,p2)
            pre = min(pre + 1, j - map[string[j]])
            ans = max(ans, pre)
            # pre = cur
            map[string[j]] = j
            # print(map)
        return ans


if __name__=="__main__":
    str = 'AAAABBCCEFCDEFGHI'
    print(Solution.LengthOfLagestSubstring(str))