# Coin Change
coins = [1,4,7,10]
target = 11
# without repeat
# [7,4], [10,1]

# [1,4,7,10]
# take = 1, target = 10, coins = [1,4,7,10]
# notTake = 0, target = 11, coins = [4,7,10]
global result
result= []

def helper(coins, i, target, path, count):
    # base
    global result
    if target == 0:
        result.append(path[:])
        return count
    if i == len(coins) or target < 0:
        return -1
    # logic
    # noChoose
    case1 =helper(coins, i+1, target, path, count)
    # choose
    path.append(coins[i])
    case2 = helper(coins, i+1, target-coins[i], path, count+1)
    path.pop()
    if case1 == -1: return case2
    if case2 == -1: return case1
    return min(case1,case2)


coins = [1,4,7,10,12]
target = 11
print(helper(coins, 0, target, [], 0))
print(result)


# with repeat
# [4,4,1,1,1], [7,1,1,1,1], [10,1]


