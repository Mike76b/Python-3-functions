# -*- coding: utf-8 -*-
"""
Created on Agu 29, 2018

@author: Mike
"""

def isPalindrome(aString):
    '''
    input of the function, aString: a string
    returning value, boolean, whether is or is not a palindrome
    '''
    # character cleaning.
    cleaning = [",", ".", " ", "?", "!", ":", ";"]
    result = aString.lower()
    for i in cleaning:
        if i in result:
            result = result.replace(i, "")
    
    # processing
    s1 = set(result[: (len(result)//2 + 2)])
    s2 = set(result[(len(result)//2) :])
    
    # returning
    return s1 == s2
    # if a deeper look is wanted, uncomment the line 27 and comment the line 25
    #return s1 == s2, result, s1, s2, len(result)



print(isPalindrome("A man, a plan, a canal: Panama!"))


