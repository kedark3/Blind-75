# Coin Change
coins = [1,4,7,10]
target = 11
# without repeat
# [7,4], [10,1]

# [1,4,7,10]
# take = 1, target = 10, coins = [1,4,7,10]
# notTake = 0, target = 11, coins = [4,7,10]
global result
result = []

def helper(coins, i, target, path):
    # base
    global result
    if target == 0:
        result.append(path[:])
        return
    if i == len(coins) or target < 0:
        return
    # logic
    # noChoose
    helper(coins, i+1, target, path)
    # choose
    path.append(coins[i])
    helper(coins, i, target-coins[i], path)
    path.pop()


coins = [1,4,7,10,12]
target = 12
helper(coins, 0, target, [])
print(result)


# with repeat
# [4,4,1,1,1], [7,1,1,1,1], [10,1]


