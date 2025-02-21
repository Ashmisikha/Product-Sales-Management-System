from database import load_data, save_data

def record_sale(product_id, quantity):
    data = load_data()
    
    product = next((p for p in data["products"] if p["id"] == product_id), None)
    if not product:
        print("❌ Product not found!")
        return

    total_price = product["price"] * quantity
    sale = {"product_id": product_id, "quantity": quantity, "total_price": total_price}
    
    data["sales"].append(sale)
    save_data(data)
    print(f"🛒 Sale recorded: {product['name']} x {quantity} - Total: ${total_price}")

def view_sales():
    data = load_data()
    if not data["sales"]:
        print("❌ No sales recorded.")
    else:
        print("\n📊 Sales History:")
        for s in data["sales"]:
            product = next((p for p in data["products"] if p["id"] == s["product_id"]), None)
            print(f"{product['name']} x {s['quantity']} - Total: ${s['total_price']}")
