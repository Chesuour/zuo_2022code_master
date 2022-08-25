"""
Data : 2022/8/25
Author : SuquanChen
Address: 出门问问 苏州


leetcode原题  难啊

给定一个字符串str. str表示一 个公式，
公式里可能有整数、加减乘除符号和左右括号
返回公式的计算结果，难点在子括号可能联套很多层
str= "48+(70-65)-43)+8+1".返回-1816。
str="3+14"返回7。 str= "3+(1+4)*1 返回7。
说明
1可以认为给定的字符事-定是正确的公式 即不需要对str做公式有效性检查
2.如果是负数就需要用括号括起来 比如“4*(-3) 但如果负数作为公式的开头或括号部分
的开头，则可以没有括号比如-3-4"和(-3*4)"都是合法的。
3不用考虑计算过程中会发生溢出的情况。
"""


# 从str[i...]往下算，遇到字符串终止位置或者右括号，就停止
# 返回两个值，长度为2的数组
# 负责的这一段的结果是多少
# 负责的这一段计算到了哪个位置



from collections import deque


class Solution():

    def calculate(s: str) -> int:
        """
        出去()内的数记录在双端队列中，最后求和，每个（）分别进行计算
        """
        def f(s):
            num, sgn, st=0, '+', deque()
            while len(s)>0:
                c = s.pop(0)
                # print(c)
                if c.isdigit():
                    num = 10*num + int(c)
                if c=='(': num = f(s)   #只要遇到小括号就去计算小括号内的数据，重新分配一个新的队列，然后返回小括号内的值
                if c in ['+','-','*','/',')'] or len(s)==0:
                    if sgn=='+': st.append(num)
                    elif sgn=='-': st.append(-num)
                    elif sgn=='*': st[-1] *= num
                    elif sgn=='/': st[-1] = int(st[-1]/num)
                    sgn, num = c, 0
                if c==')': break
                print(sgn, num)
            print(st)
            return sum(st)
        return f(list(s))


    # def ExpressionComputer(str, i):
    #     que = deque()
    #     cur = 0
    #     bra = []
    #     while i < len(str) and str[i]!= ")":
    #         if str[i]> 0 and str[i] < 9:
    #             cur = cur*10 
    #             i +=1
    #             cur = cur + str[i]
    #         elif str[i] != "(":    #遇到的是运算符号
    #             que.append(cur)
    #             i += 1
    #             que.append(str[i])
    #             cur = 0
    #         else :      #遇到左括号了
    #             bra = Solution.ExpressionComputer(str, i+1)
    #             cur = bra[0]
    #             i = bra[1] + 1
    #     pass

    # def addNum(que, num):
    #     if not que:
    #         cur = 0
    #         top = que.pop()
    #         if top == "+" or top == "-":
    #             que.append(top)
    #         else:
    #             num =(cur * num) if top.equals("*") else (cur / num)
    #     que.append(num)

    # def getNum(que):
    #     res = 0
    #     add = True
    #     num = 0
    #     cur = None
    #     while que:
    #         cur = que.leftpop()
    #         if cur == "+":
    #             add = True
    #         elif: add = False
    #         else: 
        # int res = 0;
		# boolean add = true;
		# String cur = null;
		# int num = 0;
		# while (!que.isEmpty()) {
		# 	cur = que.pollFirst();
		# 	if (cur.equals("+")) {
		# 		add = true;
		# 	} else if (cur.equals("-")) {
		# 		add = false;
		# 	} else {
		# 		num = Integer.valueOf(cur);
		# 		res += add ? num : (-num);
		# 	}
		# }
		# return res;

if __name__=="__main__":
    str = "12+(5*1)*(1+1)+1-20"
    ans = Solution.calculate(str)
    print(ans)