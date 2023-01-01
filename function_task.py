def isPalindrome(theWord): 
    reversedWord = ""
    theWord=theWord.lower()
    for letter in theWord:
        reversedWord = letter + reversedWord
        
    if (theWord == reversedWord):
        return True
    else:
        return False

if isPalindrome('Madam'):
    print("The given word is palindrome")

 
else:
    print("The given word is not palindrome")
