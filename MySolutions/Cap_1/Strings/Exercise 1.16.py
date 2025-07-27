###################################
# Exercise 1.16: String Methods
###################################

# https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/04_Strings.html


# Remember, strings are always read-only
symbols: str = 'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'

lowersyms = symbols.lower()

print('find:', symbols.find('MSFT'))

print('symbols[13:17]:', symbols[13:17])

symbols = symbols.replace('SCO', 'DOA')
print('replace:', symbols)

name = '   IBM   \n'
name = name.strip()    # Remove surrounding whitespace
print('name stripped:', name)
