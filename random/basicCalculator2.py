"""https://leetcode.com/problems/basic-calculator-ii/
TC O(n) where n is the length of the string s. We iterate over the string s at most twice.
SC O(n) where n is the length of the string s
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        currNum = 0
        res = 0
        operation = "+"
        for i,char in enumerate(s):
            # for each number character, add it to curr num
            if char.isnumeric():
                currNum = currNum * 10 + int(char)
            # check if curr char is not numeric/alpha or space OR when i=len(s)-1 i.e. when we are on the last character
            # process to calculation
            if not ( char.isnumeric() or char.isalpha() or char.isspace()) or i == len(s) -1:
                # depending on operation, push the number to the stack or calculation to the stack
                # for 1st time when we get here, we push number directly to the stack as we had set operation="+" as default
                if operation == "+":
                    stack.append(currNum)
                elif operation == "-":
                    stack.append(-currNum)  # push number with `-ve` sign
                elif operation == "*":
                    stackTop = stack.pop()  # pop the top
                    stack.append(currNum * stackTop) # multiply with currNum and push
                elif operation == "/":
                    stackTop = stack.pop() # pop the top
                    if stackTop < 0:  # perform integer division correctly
                        # to avoid wrong results, as this does floor div, negate it before div and negate the result again
                        # e.g. -3//2 = -2 vs -(--3//2)=-1 which is what we want
                        stack.append(-(-stackTop // currNum)) 
                    else:
                        stack.append(stackTop // currNum)
                # then update the operation after all if/else's are done, and currNum becomes 0
                operation = char
                currNum = 0
        while stack:
            res += stack.pop()
        
        return res
                