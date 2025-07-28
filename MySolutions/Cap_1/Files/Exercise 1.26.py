###################################
# Exercise 1.26: File Preliminaries
###################################

# https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/06_Files.html


FILE_PATH: str = r'C:\Learn\practical-python\Work\Data\portfolio.csv'

# Reading entire file at once
with open(FILE_PATH, 'rt') as f:
    data: str = f.read()

print(data)


# Although reading a file all at once is simple,
# it is often not the most appropriate way to
# do it—especially if the file happens to be
# huge or if contains lines of text that you
# want to handle one at a time.

# Reading line-by-line by iterating
with open(FILE_PATH, 'rt') as file:
    for line in file:
        print(line, end='')

