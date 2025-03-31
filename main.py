def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    return price

# Prompt user for price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount: "))

final_price = calculate_discount(price, discount_percent)
print(f"Final price: {final_price:.2f}")
