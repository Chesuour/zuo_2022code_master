"""
Data : 2022/8/9
Author : SuquanChen
Address: 出门问问 苏州

力扣691原题 贴纸拼词 困难

我们有 n 种不同的贴纸。每个贴纸上都有一个小写的英文单词。

您想要拼写出给定的字符串 target ，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。

返回你需要拼出 target 的最小贴纸数量。如果任务不可能，则返回 -1 。

注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的，并且 target 被选择为两个随机单词的连接

"""

# 有点难 暂放 学完回头写

class Solution():
    def StickersToSpellWord(stickers, target):
        print(1)
        ans = Solution.process(stickers, target)
        return -1 if ans == float("+inf") else ans

    def process(stickers, target):
        print(2)
        if len(target) == 0:
            return 0
        mini = float("+inf")
        for first in stickers:
            rest = Solution.minus(target, first)
            if len(rest) != len(target):
                rest = mini(mini, Solution.process(stickers, rest))
        return  mini + (0 if min==float("+inf") else 1)

    def minus(s1, s2):
        print(3)
        count = [0]*26
        for str in s1:
            count[ord(str) -ord('a')] +=1
        for str in s2:
            count[ord(str) - ord('a')] -=1
        bulider = []
        for i in range(26):
            if count[i] > 0:
                for j in range(count[i]):
                    bulider.append(ord(i)+'a')
        print(bulider)
        return bulider


if __name__=="__main__":
    stickers = ["with","example","science"]
    target = "thehat"
    print(Solution.StickersToSpellWord(stickers, target))