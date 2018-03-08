''' Palindrome checker using Recursion and Helper functions '''

def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    
    return isPal(toChars(s))


# Look whats going on here!
    
# toChars = it converts string into lower case and removes any non alphabet because we want uniformity.
            # all should be in one case (lower/upper) to match whether they are same or not.
            # Also special characters will always be the same . So better to remove them and then check.
            # returns a uniform string.
    
# isPal = It does the recursion part.
          # The base case is string of length one (if odd string was taken) or string of length 0 (in case of even str)
          # The recursive case is, it checks whether the first and the last alphabets are same.
          # and again calls isPal but this time for the rest of the letters s[1:-1].
          
          # The evaluation goes on until the string has been left to size 0 or 1.
          
          # If it was a palindrome, True and True = True returns from every call to isPal to previous calls.
          # so the series returns True. Which is returned by the isPalindrome() function.
          
print(isPalindrome('eve'))
print('\n')


''' To see how the True values are returned '''

def isPalindrome(s):
    
    def toChars(s):
        
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    
    def isPal(s):
        
        print("isPal is now evaluating " + s)
        
        if len(s) <= 1:
            return True
        else:
            truth_value =  s[0] == s[-1] and isPal(s[1:-1])
            print("isPal s = " +s)
            print('truth value = ',truth_value)
            return truth_value
    return isPal(toChars(s))

print(isPalindrome('civic'))


