import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ReceiptPrinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Receipt Printer")

        # Product information dictionary
        self.products = {
            "BMW": 850000,
            "TRUCK": 500000,
            "FORD MUSTANG": 3000000,
            "SUBARU": 467000
        }

        # Customer details
        self.customer_name = tk.StringVar()

        # Selected product details
        self.selected_product = tk.StringVar()
        self.selected_price = tk.StringVar()

        # Transaction history
        self.transactions = []

        self.create_widgets()

    def create_widgets(self):
        # Customer name entry
        name_label = tk.Label(self.root, text="Customer Name:")
        name_label.pack()
        name_entry = tk.Entry(self.root, textvariable=self.customer_name)
        name_entry.pack()

        # Product selection dropdown
        product_label = tk.Label(self.root, text="Select Product:")
        product_label.pack()
        product_dropdown = tk.OptionMenu(self.root, self.selected_product, *self.products.keys(), command=self.display_price)
        product_dropdown.pack()

        # Price display
        price_label = tk.Label(self.root, text="Price:")
        price_label.pack()
        price_display = tk.Label(self.root, textvariable=self.selected_price)
        price_display.pack()

        # Purchase button
        purchase_button = tk.Button(self.root, text="Purchase", command=self.purchase_product)
        purchase_button.pack()

        # Receipt preview
        receipt_label = tk.Label(self.root, text="Receipt Preview:")
        receipt_label.pack()
        self.receipt_text = tk.Text(self.root, height=10, width=50)
        self.receipt_text.pack()

        # Transaction history
        history_label = tk.Label(self.root, text="Transaction History:")
        history_label.pack()
        self.history_text = tk.Text(self.root, height=10, width=50)
        self.history_text.pack()

        # Save transaction button
        save_button = tk.Button(self.root, text="Save Transaction", command=self.save_transaction)
        save_button.pack()

    def display_price(self, selected_product):
        price = self.products[selected_product]
        self.selected_price.set(f"${price}")

    def purchase_product(self):
        customer_name = self.customer_name.get()
        selected_product = self.selected_product.get()

        if customer_name and selected_product:
            price = self.products[selected_product]
            transaction = {"Customer": customer_name, "Product": selected_product, "Price": price, "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            self.transactions.append(transaction)
            self.update_receipt_preview()
            self.update_transaction_history()
            messagebox.showinfo("Purchase Successful", f"Thank you, {customer_name}! You have purchased {selected_product} for ${price}.")
        else:
            messagebox.showerror("Error", "Please enter customer name and select a product.")

    def update_receipt_preview(self):
        self.receipt_text.delete("1.0", tk.END)
        receipt = "----------- Receipt -----------\n\n"
        receipt += f"Customer: {self.customer_name.get()}\n"
        receipt += f"Product: {self.selected_product.get()}\n"
        receipt += f"Price: ${self.selected_price.get()}\n\n"
        receipt += "--------------------------------"
        self.receipt_text.insert(tk.END, receipt)

    def update_transaction_history(self):
        self.history_text.delete("1.0", tk.END)
        history = "-------- Transaction History --------\n\n"
        for transaction in self.transactions:
            history += f"Date: {transaction['Date']}\n"
            history += f"Customer: {transaction['Customer']}\n"
            history += f"Product: {transaction['Product']}\n"
            history += f"Price: ${transaction['Price']}\n\n"
        self.history_text.insert(tk.END, history)

    def save_transaction(self):
        if self.transactions:
            filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
            with open(filename, "w") as file:
                file.write("-------- Transaction History --------\n\n")
                for transaction in self.transactions:
                    file.write(f"Date: {transaction['Date']}\n")
                    file.write(f"Customer: {transaction['Customer']}\n")
                    file.write(f"Product: {transaction['Product']}\n")
                    file.write(f"Price: ${transaction['Price']}\n\n")
            messagebox.showinfo("Transaction Saved", f"Transaction details saved to {filename}.")
        else:
            messagebox.showinfo("Transaction History", "No transactions made yet.")

# Create the GUI window
root = tk.Tk()

# Create the ReceiptPrinter object
receipt_printer = ReceiptPrinter(root)

# Run the GUI event loop
root.mainloop()




