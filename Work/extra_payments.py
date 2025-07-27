# mortgage.py
#
# Exercise 1.8

# Suppose Dave pays an extra $1000/month for the first 12
# months of the mortgage?
#
# Modify the program to incorporate this extra payment and have it print
# the total amount paid along with the number of months required.
#
# When you run the new program, it should report a total payment
# of 929,965.62 over 342 months.

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment: float = 1000  # new line
period: int = 12  # new line (months)
month: int = 1 # start month

while principal > 0:
    conditional_payment: float = payment if month  > period else payment + extra_payment
    principal = principal * (1+rate/12) - conditional_payment
    total_paid = total_paid + conditional_payment
    month += 1

print('Total paid', total_paid)