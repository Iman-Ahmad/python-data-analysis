product_name = "Laptop"
product_price = 899.99
product_quantity = 3
product_available = True

print(product_name)
print(product_price)
print(product_quantity)
print(product_available)

total_value = product_price * product_quantity
print("Total value =", total_value)

print("Variable types:")
print(type(product_name))
print(type(product_price))
print(type(product_quantity))
print(type(product_available))

print("Product status:")

if product_quantity > 0:
    print("Product is in stock")
else:
    print("Product is out of stock")

if product_available and product_quantity > 0:
    print("Product can be sold")
else:
    print("Product cannot be sold")