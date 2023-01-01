def isPalindrome(theWord):
# I created an empty variable to add reversed word in
    reversedWord = "" 
# Capital letters and lowercase letters are not equals. Because of that I lowered the word 
    theWord=theWord.lower() 
# For will take each letter of the word from left to right
# to create reversed word ,I added each letter to left of reversed
    for letter in theWord: 
        reversedWord = letter + reversedWord  
        
    if (theWord == reversedWord):
# if original word is equal to reversed word,then the word is palindrome.Function will return as True
        return True
    else:
# if original word is not equal to reversed word,then the word is not palindrome.Function will return as False
        return False

# if the function returned True
if isPalindrome('Madam'): 
    print("The given word is palindrome")
# if the function returned False 
else: 
    print("The given word is not palindrome")