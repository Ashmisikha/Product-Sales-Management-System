from products import add_product, view_products
from sales import record_sale, view_sales

def main():
    while True:
        print("\n📌 Product Sales Management System")
        print("1️⃣ Add Product")
        print("2️⃣ View Products")
        print("3️⃣ Record Sale")
        print("4️⃣ View Sales")
        print("5️⃣ Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            name = input("Product Name: ")
            category = input("Category: ")
            price = float(input("Price: "))
            add_product(name, category, price)

        elif choice == "2":
            view_products()

        elif choice == "3":
            product_id = int(input("Product ID: "))
            quantity = int(input("Quantity: "))
            record_sale(product_id, quantity)

        elif choice == "4":
            view_sales()

        elif choice == "5":
            print("🚀 Exiting program...")
            break

        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
