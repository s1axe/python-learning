products = [
    {"name": "Keyboard", "price": 2500, "stock": 10},
    {"name": "Mouse", "price": 1200, "stock": 0},
    {"name": "Monitor", "price": 15000, "stock": 5},
    {"name": "Headphones", "price": 5000, "stock": 3},
    {"name": "Webcam", "price": 3000, "stock": 0}
]

for product in products:
    if product["price"] < 5000 and product["stock"] > 0:
        print(product["name"])