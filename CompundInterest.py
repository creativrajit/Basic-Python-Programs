amount = 0

# Ask user for investment money and interest rate
principal = input("Enter your principal amoun: ")
rate = input("Your interest rate please:")

# Convert input data into float
principal = float(principal)
rate = float(rate) * 0.01

# Calculate interest for 10 years
for i in range(9):
    principal = principal + (principal * rate)

# Output amount to 2 decimal places
print("Your Expected Amount is: {:.2f}".format(principal))
