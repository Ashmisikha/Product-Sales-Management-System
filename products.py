from database import load_data, save_data

def add_product(name, category, price):
    data = load_data()
    product = {"id": len(data["products"]) + 1, "name": name, "category": category, "price": price}
    data["products"].append(product)
    save_data(data)
    print(f"✅ Product '{name}' added successfully!")

def view_products():
    data = load_data()
    if not data["products"]:
        print("❌ No products available.")
    else:
        print("\n📦 Available Products:")
        for p in data["products"]:
            print(f"{p['id']}: {p['name']} ({p['category']}) - ${p['price']}")
