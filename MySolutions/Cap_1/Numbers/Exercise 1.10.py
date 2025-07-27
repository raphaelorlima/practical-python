###################################
# Exercise 1.9: Making a Table
###################################

# https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/03_Numbers.html


# Data given in Exercise 1.9
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month: int = 61
extra_payment_end_month: int = 108
extra_payment: int = 1000

# Solution
month: int = 1
while principal > 0:
    conditional_payment: float = payment + extra_payment if \
            month >= extra_payment_start_month and \
            month <= extra_payment_end_month else payment

    principal = principal * (1+rate/12) - conditional_payment
    total_paid += conditional_payment
    month += 1

    print(
        f"Month:{round(month, 2)}, total paid:{round(total_paid, 2)}" +
        f", principal:{round(principal, 2)}"
    )
print('Total paid', total_paid)