# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
Complexity Analysis

Time complexity: 

O(4^N*N), where N is the length of digits. Note that 4 in this expression 
is referring to the maximum value length in the hash map, and not to the length of the input.
The worst-case is where the input consists of only 7s and 9s. In that case,
we have to explore 4 additional paths for every extra digit. Then, for each combination, 
it costs up to N to build the combination. This problem can be generalized to 
a scenario where numbers correspond with up to M digits, in which case the time complexity would be 
O(M ^N*N). For the problem constraints, we're given, 
M=4, because of digits 7 and 9 having 4 letters each.

Space complexity: 
O(N), where N is the length of digits.
Not counting space used for the output, the extra space we use relative 
to input size is the space occupied by the recursion call stack.
It will only go as deep as the number of digits in the input since whenever we reach that depth, we backtrack.

"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0: 
            return []
        
        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append(''.join(path))
                return
            
            for letter in letters[digits[index]]:
                # action
                path.append(letter)
                #recurse
                backtrack(index+1, path)
                #backtrack
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations