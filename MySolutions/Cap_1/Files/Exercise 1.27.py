###################################
# Exercise 1.27: Reading a data file
###################################

# https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/06_Files.html

from functions import pcost

FILE_PATH: str = 'practical-python\Work\Data\portfolio.csv'

sum: float = pcost(FILE_PATH)
print('Total cost', sum)