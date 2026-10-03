# -------------------------
# 1. Lists
# -------------------------

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

products.append("Headphones")
products.append("Webcam")

print("Products:")
print(products)

print("Number of products:", len(products))

print("Products with indexes:")

for index, product in enumerate(products):
    print(index, product)


# -------------------------
# 2. Conditions
# -------------------------

print("Searching for Laptop:")

for product in products:
    if product == "Laptop":
        print(product, "is the main product")
    else:
        print(product, "is another product")


# -------------------------
# 3. Dictionary
# -------------------------

product = {
    "name": "Laptop",
    "price": 899.99,
    "quantity": 3,
    "available": True
}

print("Top product:", product)

print("Product's name:", product["name"])

product["quantity"] = 5

print("Updated quantity:", product["quantity"])


# -------------------------
# 4. List of dictionaries
# -------------------------

products_data = [
    {
        "name": "Laptop",
        "price": 899.99,
        "quantity": 5,
        "available": True
    },
    {
        "name": "Mouse",
        "price": 29.99,
        "quantity": 12,
        "available": True
    },
    {
        "name": "Keyboard",
        "price": 59.99,
        "quantity": 0,
        "available": False
    }
]


# -------------------------
# 5. Stock analysis
# -------------------------

total_stock_value = 0

for product in products_data:
    stock_value = product["price"] * product["quantity"]

    total_stock_value = total_stock_value + stock_value

    print(product["name"], "-", stock_value)

    if product["available"] and product["quantity"] > 0:
        print(product["name"], "is in stock")

print("Total stock value:", total_stock_value)