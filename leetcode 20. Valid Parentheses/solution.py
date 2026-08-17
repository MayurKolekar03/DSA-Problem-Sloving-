class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in mapping:
            
                top_ele = stack.pop() if stack else "#"

                if mapping[i] != top_ele:
                    return False
            else:
                stack.append(i)
        return not stack
        
