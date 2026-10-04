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
# 2. File Handling
# -------------------------

try:
    with open("products.txt", "r") as file:
        products_from_file = file.read().splitlines()

    print("Products from file:")

    for product in products_from_file:
        print(product)

except FileNotFoundError:
    print("The file was not found") 
# -------------------------
# 3. Conditions
# -------------------------

print("Searching for Laptop:")

for product in products:
    if product == "Laptop":
        print(product, "is the main product")
    else:
        print(product, "is another product")


# -------------------------
# 4. Dictionary
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
# 5. List of dictionaries
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
# 6. Stock analysis & Functions
# -------------------------

def calculate_stock_value(product):
    return product["price"] * product["quantity"]

def is_product_in_stock(product):
    return product["available"] and product["quantity"] > 0

total_stock_value = 0

for product in products_data:
    stock_value = calculate_stock_value(product)

    total_stock_value = total_stock_value + stock_value

    print(product["name"], "-", stock_value)

    if is_product_in_stock(product):
        print(product["name"], "is in stock")

print("Total stock value:", total_stock_value)

# -------------------------
# 7. Write a stock report
# -------------------------

with open("stock_report.txt", "w") as file:
    for product in products_data:
        stock_value = calculate_stock_value(product)

        file.write(f"{product['name']}: {stock_value}\n")

# -------------------------
# 8. append to a stock report
# -------------------------

with open("stock_report.txt", "a") as file:
    file.write("Report generated successfully.\n")