def  calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

price= float(input("Enter the price of the item: "))
discount_percent= float(input("Enter the discount percentage: "))

final_amount= calculate_discount(price, discount_percent)
print(f"The total amount after discount is: {final_amount}")
