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


"""
先删除多余右括号，再反转字符串，同样方法删除多余左括号。原理是只要括号相同数量，且没有“)(”的情况则一定valid。比解法二快。

递归函数的参数中，last_i表示当前遍历到的位置，相当解法二中的start，last_j表示上一个删除的位置，c表明现在需要删除的是多余的左括号还是右括号。

在递归函数中，从last_i开始遍历，在删除右括号的时候，count表示统计到当前位置i时右括号出现的次数，遇到右括号增加1，遇到左括号减1。
这里遇到右括号为正，即进入第二层for循环进行删除，可以防止字符串开头是)(反向括号的情况，反之删除左括号时亦然。

count大于0的时候，说明到当前位置i右括号多，即进入第二层for循环开始删除多余右括号：从上一个删除位置last_j开始遍历到当前位置i，如果当前是右括号，且是第一个右括号，删除当前右括号，并继续调用递归函数。
注意！此第二层for循环结束后要直接返回，必须加return，否则会继续进入下面的翻转操作。因为进这个for循环的是右括号多的，不断递归删到最后最多是删成和左括号一样多，不需要再去翻转删左括号。

count小于等于0时，即当前左括号数量大于等于右括号，直接跳过不进入第二层for循环，继续往右遍历统计“)”，即也不会return；
整个字符串统计完以后，而是将字符串反转一下，此时反向括号“)(”是valid，继续调用递归函数删除多余的左括号，last_i和last_j均重置为0。

反转后调用递归函数时需要判断一下c：如果是右括号，说明现在开始要删除左括号；如果是左括号，说明反转已经进行过，那么就可以直接加入结果res了。
"""

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



    def removeInvalidParentheses( s):
        global res 
        res = []
        Solution.DFS(s, ')', 0, 0)
        return res
    
    def DFS( s, c, last_i, last_j):
        count = 0
        for i in range(last_i, len(s)):
            if s[i] == '(' or s[i] == ')':
                if s[i] == c: count += 1
                else: count -= 1
            if count <= 0: continue
            for j in range(last_j, i+1):
                if s[j] == c and (j == last_j or s[j] != s[j-1]):
                    Solution.DFS(s[:j] + s[j+1:], c, i, j)
            return #break out of DFS function directly
        s = list(s)[::-1]
        s = ''.join(s)
        if c == ')': Solution.DFS(s, '(', 0, 0)
        else: res.append(s)


if __name__=="__main__":
    sss = ['(',')','(',')',')','(',')']
    # print("+++++++"+sss[6]+"+++++++")
    print(Solution.generateParenthesis(sss))
    print(Solution.removeInvalidParentheses(sss))