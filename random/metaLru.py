# Add any extra import statements you may need here


# Add any helper functions you may need here
class Node:
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.next = None
    self.prev = None


class LRUCache: 
  
  
  def __init__(self, capacity):
    # store DLL nodes in the hasmap with their values as key
    self.cache = {} # helps us get O(1) lookup time
    self.cap = capacity
    self.head = Node(-1,-1)
    self.tail = Node(-1,-1)
    self.head.next = self.tail
    self.tail.prev = self.head
    
  def _move_to_head(self, node):
    self._remove_node(node)
    self._add_node(node)
    
  def _remove_node(self,node):
    p = node
    p.prev.next = p.next
    p.next.prev = p.prev
    p.prev = None
    p.next = None
    
  def _add_node(self,node):
    p = self.head
    node.prev = p
    node.next = p.next
    p.next = node
    node.next.prev = node
    
  def _pop_tail(self):
    node = self.tail.prev
    self._remove_node(node)
    

  def get(self, x):
    # when we want to get the node, look it up in the cache
    if x in self.cache:
      node = self.cache[x]
      self._move_to_head(node)
      return node.val
    return -1

  def set(self, x, y):
    # Write your code here
    if x in self.cache:
      node = self.cache[x]
      self._move_to_head(node)
      node.val = y
    else:
      if len(self.cache) > self.cap:
        self._pop_tail()
      node = Node(x,y)
      self._add_node(node)
      self.cache[x] = node
        
      




# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', expected, sep='', end='')
    print(' Your output: ', output, end='')
    print()
  test_case_number += 1

if __name__ == "__main__":
  cacheOne = LRUCache(2) 
  cacheOne.set(1, 2)
  outputOne = [cacheOne.get(1)]
  check([2], outputOne)

  cacheTwo = LRUCache(2)
  cacheTwo.set(1,2)
  cacheTwo.set(2,3)
  cacheTwo.set(1,5)
  cacheTwo.set(4,5)
  cacheTwo.set(6,7)
  outputTwo = [cacheTwo.get(4)]
  cacheTwo.set(1,2)
  outputTwo.append(cacheTwo.get(3))
  check([5, -1], outputTwo)

  # Add your own test cases here
  

