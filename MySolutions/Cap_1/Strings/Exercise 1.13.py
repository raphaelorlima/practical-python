###################################
# Exercise 1.13: Making a Table
###################################

# https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/04_Strings.html

symbols = 'AAPL,IBM,MSFT,YHOO,SCO'

for i in range(-2,3):
    print(i, symbols[i])
    

# In Python, strings are read-only.
# Verify this by trying to change the first character of
# symbols to a lower-case ‘a’.

symbols[0] = 'a'