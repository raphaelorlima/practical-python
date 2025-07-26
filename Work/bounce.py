# bounce.py
#
# Exercise 1.5

height: int = 100 # meters

bounce_number: int = 0
while bounce_number <= 10:
    bounce_number += 1
    height: float = 0.6 * float(height)
    print(f"Bounce number: {bounce_number}; height: {round(height,2)}")