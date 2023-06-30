# all comments are mine (amnolan)
# A is the input array, val is the sought after value
def find_sum_of_two(A, val):
  
  # first time it will be empty but gradually we will fill until we find a match
  # this prevents us having to visit the same item twice making performance N
  # use a set() (hashset) for efficiency purposes
  found_items = set()

  for a in A:
    # this is using the complement of the sought value by subtracting the current value for instance
    # if val is 30 and the input list looks like this: {16, 14, 2, 5, 9}
    # and found_items looks like this: {16}
    # when the iterator steps to the value 14 then it does math like: val - a in found_items? ... 30 - 16 = any value?
    # when it sees 30 - 16 = 14 it will return True
    
    if val - a in found_items:  
      return True
      
    # if not found, continue adding to the list
    found_items.add(a)
  return False
