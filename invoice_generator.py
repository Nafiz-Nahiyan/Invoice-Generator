from datetime import datetime

class InvoiceGenerator:
    def __init__(self):
        self.client_details = {}
        self.items = []
        self.total = 0

    def get_client_details(self):
        self.client_details['name'] = input("Enter client name: ")
        self.client_details['address'] = input("Enter client address: ")
        self.client_details['email'] = input("Enter client email: ")
    
    def add_item(self):
        item_name = input("Enter item name: ")
        quantity = int(input(f"Enter quantity of {item_name}: "))
        price = float(input(f"Enter price per unit of {item_name}: "))
        total_price = quantity * price
        self.items.append({
            'name': item_name,
            'quantity': quantity,
            'price': price,
            'total': total_price
        })
        self.total += total_price

    def generate_invoice(self):
        invoice_num = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"invoice_{invoice_num}.txt"
        
        with open(file_name, "w") as file:
            file.write("===== INVOICE =====\n")
            file.write(f"Invoice Number: {invoice_num}\n")
            file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            file.write(f"Client Name: {self.client_details['name']}\n")
            file.write(f"Address: {self.client_details['address']}\n")
            file.write(f"Email: {self.client_details['email']}\n\n")
            
            file.write("===== ITEMS =====\n")
            for item in self.items:
                file.write(f"{item['name']} | Qty: {item['quantity']} | Price: {item['price']} | Total: {item['total']}\n")
            
            file.write(f"\nTotal Amount: ${self.total:.2f}\n")
            file.write("===================\n")

        print(f"Invoice generated: {file_name}")

def main():
    invoice = InvoiceGenerator()
    
    print("=== Client Details ===")
    invoice.get_client_details()

    while True:
        print("\n=== Add Item ===")
        invoice.add_item()
        more_items = input("Add another item? (y/n): ")
        if more_items.lower() != 'y':
            break

    invoice.generate_invoice()

if __name__ == "__main__":
    main()
