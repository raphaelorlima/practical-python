###################################
# Exercise 1.14: String concatenation
###################################

# https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/04_Strings.html

symbols = 'AAPL,IBM,MSFT,YHOO,SCO'

# symbols = symbols + 'GOOG'  # original
symbols = ','.join([symbols, 'GOOG'])
print(symbols)


# Add 'HPQ' to the front the string:

symbols = 'HPQ,' + symbols
symbols