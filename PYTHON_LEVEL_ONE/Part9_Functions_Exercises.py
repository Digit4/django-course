#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
  for i, v in enumerate(nums):
    if (i + 2 >= len(nums)):
      return False
    if (v == 1):
      if (nums[i + 1] == 2):
        if (nums[i + 2] == 3):
          return True


print(arrayCheck([1, 1, 2, 3, 1]),
arrayCheck([1, 1, 2, 4, 1]),
arrayCheck([1, 1, 2, 1, 2, 3]))


#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
  new_str_arr = []
  for i,v in enumerate(str):
    if (i % 2 == 0):
      new_str_arr.append(v)
  return "".join(new_str_arr)
    

print(stringBits('Hello'), stringBits('Hi'), stringBits('Heeololeo'))


#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
  alen,blen = len(a),len(b)
  if (alen > blen):
    return end_check(a, b, blen)
  else:
    return end_check(b, a, alen)

    
def end_check(x, y, itr):
  flag = False
  xlen = len(x)
  for i in range(itr - 1, 0, -1):
    xlen -= 1
    if (y[i].lower() == x[xlen].lower()):
      flag = True
    else:
      flag = False
  
  return flag


print(end_other('Hiabc', 'abc'), end_other(
    'AbC', 'HiaBc'), end_other('abc', 'abXabc'))
#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(string):
  ar = list(map(str, string))
  new_arr = []
  for i in ar:
    new_arr.append(i)
    new_arr.append(i)
  return "".join(new_arr)


print(doubleChar("The"))

#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
  a, b, c = fix_teen(a), fix_teen(b), fix_teen(c)
  return (a + b + c)

def fix_teen(n):
  if (n >= 13 and n <= 19):
    if (n != 15 and n != 16):
      return 0
  return n

print(no_teen_sum(1, 2, 3), no_teen_sum(2, 13, 1), no_teen_sum(2, 1, 14))

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
  pass# CODE GOES HERE
