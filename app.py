products = [
    {"id": 1, "name": "Laptop", "price": 45000},
    {"id": 2, "name": "Headphones", "price": 1500},
    {"id": 3, "name": "Keyboard", "price": 800},
]


def get_products():
    return products


if __name__ == "__main__":
    print("Welcome to E-Commerce Platform!")
    print("Available Products:")

    for product in get_products():
        print(f'{product["id"]}. {product["name"]} - Rs.{product["price"]}')