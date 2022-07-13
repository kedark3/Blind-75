"""To Increase efficiency, the Amazon shipping team will
group packages being shipped according to weight. They will
merge a lighter package with a heavier package, which eliminates
the need for separate shipments.
More formally, consider n packages, where package Weights[i]
represents the welght of the f' package. You can combine the th
and (i+1) '" package if packageWeights(i) < packageWeightsli+ 1),
then discard the f" package. After this operation, the number of
packages is reduced by 1 and the weight of the (i+1)(" package
Increases by packageWeights(I). You can merge the packages any
number of times.
Find the maximum possible welght of a package that can be
achleved after any sequence of merge-operations.
Example
For example, packages are described as package weights = [2, 9,
10, 3, 71.
The optimal order of operations Is, using 1-based indexing:
• Combine the packages at index 2 and index 3, the new array
of package weights becomes [2, 19, 3, 7]
• Combine the packages at index 1 and index 2, the new array
of package welghts becomes [21, 3, 7].
• Combine the packages at index 2 and Index 3, the new array of
package weights becomes [21, 10].
We can not combine the packages anymore.
The weight of the heavlest package achlevable after merging is
21
"""

# Approach 1: Iterative - left to right
def getHeaviestPackage(packageWeights):
    res = []
    i = 1
    curr_sum = packageWeights[0]
    while i < len(packageWeights):
        # at each step - greedily add weight of package to currSum as long as next package is heavier than current
        if packageWeights[i] > packageWeights[i-1]:
            curr_sum += packageWeights[i]
        else: # packageWeights[i] < packageWeights[i-1]:
            # when it is no longer true, add that sum to result list and reset curr_sum to current Package weight 
            res.append(curr_sum)
            curr_sum = packageWeights[i]
        # if we reach the end of the list we should add whatever we have thus far to result            
        if (i+1) == len(packageWeights):
            res.append(curr_sum)
            i = 0 # then reset i to 0
            # if we come here again and our packageweights and result len is equal
            # that means we can't improve heaviest package anymore, exit the loop
            if len(packageWeights) == len(res):
                break
            # else update packageWeights to point to res
            packageWeights = res
            # and reset result to empty list
            res = []
            # set curr_sum again to 1st package weight but remember this time
            # we are really setting it to first wt from our result of this iteration
            # see line #51
            curr_sum = packageWeights[0]
            # and continue merging packages again
        # keep incrementing i in all cases
        i += 1
    # if we print pacakgeWeights, it gives us exact weights we got after merging
    # and max of it will give us maximum package weight
    return max(packageWeights)

# print(getHeaviestPackage([2,9,10,3,7]))
# print(getHeaviestPackage([50]))
# print(getHeaviestPackage([20,13,8,9]))
# print(getHeaviestPackage([30,15,5,9]))


# Approach : right to left 1 pass linear
def getHeaviestPackage2(packageWeights):
    # base case
    if len(packageWeights) == 0:
        return 0
    
    n = len(packageWeights)
    # set cur and res to last element
    cur = res = packageWeights[n-1]
    # loop from 2nd last element to 0th element
    for i in range(n-2, -1, -1):
        # if wt of ith pkg is less than cur so far, we can add that to cur
        if packageWeights[i] < cur:
            cur += packageWeights[i]
        else:# if not, then cur resets to wt of ith pkg
            cur = packageWeights[i]
        # in either case we need to update the res
        res = max(res, cur)
    # return result holding max pkg weight. This approach doesn't give use the exact package weights
    # for all of the packages after merging. It just gives max weight
    return res

# print(getHeaviestPackage2([2,9,10,3,7]))
# print(getHeaviestPackage2([50]))
# print(getHeaviestPackage2([20,13,8,9]))
# print(getHeaviestPackage2([30,15,5,9]))

import unittest

class TestHeaviestPackage(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(getHeaviestPackage2([2,9,10,3,7]),getHeaviestPackage([2,9,10,3,7]))
        self.assertEqual(getHeaviestPackage2([50]),getHeaviestPackage([50]))
        self.assertEqual(getHeaviestPackage2([20,13,8,9]),getHeaviestPackage([20,13,8,9]))
        self.assertEqual(getHeaviestPackage2([30,15,5,9]),getHeaviestPackage([30,15,5,9]))

if __name__ == "__main__": unittest.main()