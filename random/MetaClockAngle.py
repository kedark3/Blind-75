import math

def getSmallestClockAngle(timeString, unit):
  # Write your code here
  # findings
  # for mins you multiply min * 6 to get exact degrees
  # for hours you multiply hour * 30 + min * 1/2 to get degrees
  # if angle of result is bigger than 180 - then subtract 180 from it to find
  # minimum angle
  # degree to radian can be converted as degree * pi(3.14)/180
  
  # parse the string
  splits = timeString.split(':')
  
  hr = int(splits[0])
  mi = int(splits[1])
 
  min_degree = mi * 6
  hr_degree = hr  * 30 + mi / 2
  total_degree = abs(hr_degree - min_degree)
  if total_degree > 180:
    total_degree -= 180
  if unit == 'radians':
    total_degree = round(total_degree * (math.pi/180), 4)
  
  return total_degree












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
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', expected, sep='', end='')
    print(' Your output: ', output, end='')
    print()
  test_case_number += 1

if __name__ == "__main__":
  output_1 = getSmallestClockAngle('03:00', 'radians')
  check(1.5708, output_1)

  output_2 = getSmallestClockAngle('09:30', 'degrees')
  check(105, output_2)

