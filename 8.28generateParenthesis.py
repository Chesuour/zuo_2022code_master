"""
Data : 2022/8/25
Author : SuquanChen
Address: 出门问问 苏州

301. 删除无效的括号 leetcode 原题 难
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 任意顺序 返回。

输入：s = "()())()"
输出：["(())()","()()()"]

输入：s = "(a)())()"
输出：["(a())()","(a)()()"]

输入：s = ")("
输出：[""]
"""

   # // modifyIndex <= checkIndex
	# // 只查s[checkIndex....]的部分，因为之前的一定已经调整对了
	# // 但是之前的部分是怎么调整对的，调整到了哪？就是modifyIndex
	# // 比如：
	# // ( ( ) ( ) ) ) ...
	# // 0 1 2 3 4 5 6
	# // 一开始当然checkIndex = 0，modifyIndex = 0
	# // 当查到6的时候，发现不对了，
	# // 然后可以去掉2位置、4位置的 )，都可以
	# // 如果去掉2位置的 ), 那么下一步就是
	# // ( ( ( ) ) ) ...
	# // 0 1 2 3 4 5 6
	# // checkIndex = 6 ，modifyIndex = 2
	# // 如果去掉4位置的 ), 那么下一步就是
	# // ( ( ) ( ) ) ...
	# // 0 1 2 3 4 5 6
	# // checkIndex = 6 ，modifyIndex = 4
	# // 也就是说，
	# // checkIndex和modifyIndex，分别表示查的开始 和 调的开始，之前的都不用管了  par  (  )

class Solution():
    def generateParenthesis(s):
        # List<String> ans = new ArrayList<>();
		# remove(s, ans, 0, 0, new char[] { '(', ')' });
		# return ans;
        global N, par
        ans = []
        par = ['(',')']
        N = len(s)
        Solution.move(s ,ans, 0 ,0, par)
        return ans
    def move(s, ans, checkindex, deleteindex, par):
        for i in range(checkindex ,N):
            count = 0
            # print(i)
            # print(s[i])
            if s[i] == par[0]:
                count += 1
            if s[i] == par[1]:
                count -= 1
            if count < 0:
                for j in range(deleteindex, i+1):
                    j +=1
                    if s[j] == par[1] and (j == deleteindex or s[j-1] != par[1]):
                         Solution.move(s[0:j-1]+s[j+1: N], ans, i, j, par)
                return
        reversed_str = s.reverse()
        par_reversed = [')','(']
        if par[0] == '(':
             Solution.move(reversed_str, ans, 0, 0, par_reversed)
        else:
            ans.append(reversed_str)        


if __name__=="__main__":
    sss = ['(',')','(',')',')','(',')']
    # print("+++++++"+sss[6]+"+++++++")
    print(Solution.generateParenthesis(sss))