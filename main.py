products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

products.append("Headphones")
products.append("Webcam")

print("Products:")
print(products)

print("Number of products:", len(products))

print("Products with indexes:")
for index, product in enumerate(products):
    print(index, product)

print("Searching for Laptop:")
for product in products:
    if product == "Laptop":
        print(product, "is the main product")
    else:
        print(product, "is another product")