# Jane Doe
# 20 MAY 2026
# Sample Python Script

# Prompt the user for their first name
first_name = input("Please enter your first name: ")

# What does the next line of code do?
print(f"\nWelcome, {first_name.title( )}!\n")

# What is Python doing in this block of code?
appetizer = 6.99
beverage1 = 2.50
beverage2 = 2.75
dinner1 = 18.00
dinner2 = 22.00
dessert1 = 9.75
dessert2 = 8.99

subtotal = appetizer + beverage1 + beverage2 + dinner1 + dinner2 + dessert1 + dessert2

# In programming terminology, what’s the difference between TIP_RATE and dinner1 or dessert2, for example?
TAX_RATE = 0.06
TIP_RATE = 0.20

# What is Python trying to calculate in the next three lines of code?
state_tax = subtotal * TAX_RATE
tip = subtotal * TIP_RATE
grand_total = subtotal + state_tax + tip

# What do you think the .2f means in some of the print statements below?
print(f"\n--- Bill Summary for {first_name} ---")
print(f"Subtotal:        ${subtotal:.2f}")
print(f"State Sales Tax: ${state_tax:.2f}")
print(f"Tip (20%):       ${tip:.2f}")
print(f"Grand Total:     ${grand_total:.2f}")

