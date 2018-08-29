# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 12:07:38 2018

@author: Mike
"""


def isPalindrome(aString):
    '''
    aString: a string
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
    
    #returning
    return s1 == s2#, result, s1, s2, len(result) 



print(isPalindrome("A man, a plan, a canal: Panama!"))
        














