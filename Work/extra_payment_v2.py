# extra_payment_v2.py
#
# Exercise 1.9
#
# Modify the program so that extra payment information can be more generally
# handled. Make it so that the user can set these variables:
#
# extra_payment_start_month = 61
# extra_payment_end_month = 108
# extra_payment = 1000
#
# Make the program look at these variables and calculate the total paid
# appropriately.
#
# How much will Dave pay if he pays an extra $1000/month for 4 years
# starting after the
# first five years have already been paid?

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month: int = 61
extra_payment_end_month: int = 108
extra_payment: int = 1000

month: int = 1
while principal > 0:
    conditional_payment: float = payment + extra_payment if month >= extra_payment_start_month and month <= extra_payment_end_month else payment
    principal = principal * (1+rate/12) - conditional_payment
    total_paid += conditional_payment
    month += 1
    
    if conditional_payment < principal:
        conditional_payment = payment  # last payment cannot be negative
    
    # print (f"Month:{round(month,2)}, total paid:{round(total_paid,2)}, principal:{round(principal,2)}, percentual:{round(float(total_paid/principal),1)}%")  # test

print('Total paid', total_paid)

