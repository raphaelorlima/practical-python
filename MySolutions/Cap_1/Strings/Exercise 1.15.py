###################################
# Exercise 1.15: Membership testing (substring testing)
###################################

# https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/04_Strings.html


symbols: str = 'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'

print('IBM' in symbols)
print('AA' in symbols)
print('CAT' in symbols)

# Why did the check for 'AA' return True?
# Answer: Because it's true the string 'AA' are in 'symbols'. 
