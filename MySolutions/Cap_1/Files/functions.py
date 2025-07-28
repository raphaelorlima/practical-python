
# Write a program called pcost.py that opens this file,
# reads all lines, and calculates how much it cost to
# purchase all of the shares in the portfolio.

# Convert string to list
def _tolist(string: str, sep: str = ','):
    return string.split(sep)

def pcost(path: str):

    rows: list = []   # Empty list

    # Treating file
    with open(path, 'rt') as file:
        for line in file:
            line = line.replace("\n", '')    # Cleaning lines
            line = line.replace('"', '')     # Cleaning lines
            line = _tolist(line)             # Converting to list
            rows.append(line)         # Add empty list

    sum = 0
    for i in rows[-7:]:
        sum = (float(i[1])*float(i[2])) + sum

    return sum
