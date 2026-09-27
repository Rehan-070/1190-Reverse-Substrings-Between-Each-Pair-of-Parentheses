# class Solution:
#     def reverseParentheses(self, s: str) -> str:
#         n = len(s)
#         pair = [0] * n
#         st = []
#         for i in range(n):
#             if s[i] == '(':
#                 st.append(i)
#             elif s[i] == ')':
#                 j = st.pop()
#                 pair[i] = j
#                 pair[j] = i
#         res = []
#         i, dir = 0, 1
#         while 0 <= i < n:
#             if s[i] in '()':
#                 i = pair[i]
#                 dir = -dir
#             else:
#                 res.append(s[i])
#             i += dir
#         return ''.join(res)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]

        for ch in s:
            if ch == '(':
                stack.append("")
            elif ch == ')':
                temp = stack.pop()
                stack[-1] += temp[::-1]
            else:
                stack[-1] += ch

        return stack[0]
