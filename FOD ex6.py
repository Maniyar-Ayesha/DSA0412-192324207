# Item prices and quantities
prices = [100, 200, 50]        # Example: 3 items
quantities = [2, 1, 4]

# Discount and tax rates (in percentages)
discount_rate = 10   # 10%
tax_rate = 5         # 5%

# Step 1: Calculate subtotal
subtotal = sum([price * qty for price, qty in zip(prices, quantities)])

# Step 2: Apply discount
discount_amount = (discount_rate / 100) * subtotal
amount_after_discount = subtotal - discount_amount

# Step 3: Apply tax
tax_amount = (tax_rate / 100) * amount_after_discount
total_cost = amount_after_discount + tax_amount

# Print results
print(f"Subtotal: ₹{subtotal}")
print(f"Discount: ₹{discount_amount}")
print(f"Amount after Discount: ₹{amount_after_discount}")
print(f"Tax: ₹{tax_amount}")
print(f"Total Cost to Customer: ₹{total_cost}")
