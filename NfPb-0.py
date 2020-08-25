def toString(list):
  ''' create empty string to be return to the function once it is completed the way while
  want it ''' 
  newString = '\'' #add first ' 
  
  for i in range (len(list) -1): # the last item on the list would be different from the                               #prev ones.  
    newString += list [i] + ', ' # all the elements will be added to the "newString" and                             # separated by a comma except for the last element 
    
  newString += 'and ' + list[-1] + '\'' # we add 'and',the last element of the list to the new                               # string  and the single quote at the end
  return newString # we return instead of printing

spam = ['apples', 'bananas', 'tofu', 'cats', 'dog', 'pet']

print(toString(spam))
    