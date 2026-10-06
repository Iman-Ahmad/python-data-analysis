import csv
import pandas as pd

# -------------------------
# 1. Lists
# -------------------------

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

products.append("Headphones")
products.append("Webcam")

#print("Products:")
#print(products)

#print("Number of products:", len(products))

#print("Products with indexes:")

for index, product in enumerate(products):
    print(index, product)

# -------------------------
# 2. File Handling
# -------------------------

try:
    with open("products.txt", "r") as file:
        products_from_file = file.read().splitlines()

    #print("Products from file:")

    #for product in products_from_file:
    #    print(product)

except FileNotFoundError:
    print("The file was not found") 

# -------------------------
# 3. CSV File
# -------------------------

#with open("products.csv", "r") as file:
#    reader = csv.DictReader(file)

#    for product in reader:
#        price = float(product["price"])
#        quantity = int(product["quantity"])

#        print(product["name"], "-", price * quantity)

# -------------------------
# 4. Pandas
# -------------------------

products_df = pd.read_csv("products.csv")

#print("DataFrame shape: ")
#print(products_df.shape)

print("Missing values: ")
print(products_df.isna().sum())

print("Number of duplicate rows: ")
print(products_df.duplicated().sum())

print("Duplicate rows: ")
print(products_df[products_df.duplicated()])

products_df["price"] = (products_df["price"].astype(str).str.replace(" USD", "", regex=False))
products_df["price"] = pd.to_numeric(products_df["price"], errors="coerce")

products_df = products_df.drop_duplicates()

electronics_median_price = products_df[products_df["category"] == "Electronics"]["price"].median()

products_df["price"] = products_df["price"].fillna(electronics_median_price)

print("DataFrame after removing duplicates: ")
print(products_df)

print("Number of rows after removing duplicates: ")
print(len(products_df))

print("Missing values after cleaning:")
print(products_df.isna().sum())

print("Duplicate rows after cleaning:")
print(products_df.duplicated().sum())
print(products_df[products_df.duplicated()])

print("Electronics median price:", electronics_median_price)

electronics_prices = products_df[products_df["category"] == "Electronics"]["price"]

print("Electronics average price: ", electronics_prices.mean())
print("Electronics median price: ", electronics_prices.median())

print("DataFrame after filling missing prices:")
print(products_df)

print("Data types: ")
print(products_df.dtypes)

#print("Products DataFrame:")
#print(products_df)

#print("Columns:")
#print(products_df.columns)

#print("Data types:")
#print(products_df.dtypes)

products_df["stock_value"] = (products_df["price"] * products_df["quantity"])

total_stock_value = products_df["stock_value"].sum()
#print("Total stock value: ", total_stock_value)

average_product_price = products_df["price"].mean()
#print("Average product price:", round(average_product_price, 2))

stock_value_by_category = products_df.groupby("category")["stock_value"].sum()

#print("Stock value by category: ")
#print(stock_value_by_category)

category_summary = products_df.groupby("category").agg(average_price=("price", "mean"), product_count=("name", "count"), total_quantity=("quantity", "sum"))

#print("Category summary: ")
#print(category_summary)

highest_price = products_df["price"].max()
highest_price_index = products_df["price"].idxmax()
highest_price_product = products_df.loc[highest_price_index]

#print("Highest product price: ", highest_price)
#print("highest priced product: ", highest_price_product)

lowest_price = products_df["price"].min()
#print("Lowest product price: ", lowest_price)

#print("DataFrame with stock value:")
#print(products_df)

#print(products_df.iloc[0])
#print(products_df.iloc[0:3])

# -------------------------
# 5. Pandas Filtering
# -------------------------

in_stock_products = products_df[products_df["quantity"] > 0]

#print("Products in stock:")
#print(in_stock_products)

filtered_products = products_df[(products_df["quantity"] > 0) & (products_df["price"] > 50)]

#print("Products in stock and price above 50:")
#print(filtered_products)

# -------------------------
# 6. Conditions
# -------------------------

#print("Searching for Laptop:")

#for product in products:
#    if product == "Laptop":
#        print(product, "is the main product")
#    else:
#        print(product, "is another product")

# -------------------------
# 7. Dictionary
# -------------------------

product = {
    "name": "Laptop",
    "price": 899.99,
    "quantity": 3,
    "available": True
}

#print("Top product:", product)

#print("Product's name:", product["name"])

product["quantity"] = 5

#print("Updated quantity:", product["quantity"])


# -------------------------
# 8. List of dictionaries
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
# 9. Stock analysis & Functions
# -------------------------

def calculate_stock_value(product):
    return product["price"] * product["quantity"]

def is_product_in_stock(product):
    return product["available"] and product["quantity"] > 0

total_stock_value = 0

for product in products_data:
    stock_value = calculate_stock_value(product)

    total_stock_value = total_stock_value + stock_value

#    print(product["name"], "-", stock_value)

#    if is_product_in_stock(product):
#       print(product["name"], "is in stock")

#print("Total stock value:", total_stock_value)

# -------------------------
# 10. Write a stock report
# -------------------------

with open("stock_report.txt", "w") as file:
    for product in products_data:
        stock_value = calculate_stock_value(product)

        file.write(f"{product['name']}: {stock_value}\n")

# -------------------------
# 11. append to a stock report
# -------------------------

with open("stock_report.txt", "a") as file:
    file.write("Report generated successfully.\n")