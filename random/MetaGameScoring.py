

def gameScoring(score):
  # Write your code here
  result = []
  
  def helper(arr, score, index, currSum, path, result):    
    # base case
    if currSum == score:
        result.append(path[:]) 
        return result
    if currSum > score:
        return result
    # logic
    for i in range(0,len(arr)):
        # action
        path.append(arr[i])
        # recurse
        helper(arr, score, i, currSum + arr[i], path, result)
        # backtrack
        path.pop()
    
    return result
  result = helper([1,2,3], score, 0, 0, [], result)
  return result


print(gameScoring(4))