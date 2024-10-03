import tkinter as tk
from tkinter import messagebox, simpledialog

# This is a simple contact manager app
class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("500x600")
        self.contacts = []  # This will store all contacts

        # Title of the app
        self.title_label = tk.Label(root, text="Contact Manager", font=("Arial", 20), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # Input frame for new contact details
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        # Name input
        self.name_label = tk.Label(self.input_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.input_frame, width=30)
        self.name_entry.grid(row=0, column=1)

        # Phone input
        self.phone_label = tk.Label(self.input_frame, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.input_frame, width=30)
        self.phone_entry.grid(row=1, column=1)

        # Email input
        self.email_label = tk.Label(self.input_frame, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.input_frame, width=30)
        self.email_entry.grid(row=2, column=1)

        # Address input
        self.address_label = tk.Label(self.input_frame, text="Address:")
        self.address_label.grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.input_frame, width=30)
        self.address_entry.grid(row=3, column=1)

        # Frame for buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Add Contact Button
        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=0, column=0, padx=10)

        # View Contacts Button
        self.view_button = tk.Button(self.button_frame, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=0, column=1, padx=10)

        # Search Contact Button
        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=0, column=2, padx=10)

        # Update Contact Button
        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=1, column=0, padx=10)

        # Delete Contact Button
        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=1, column=1, padx=10)

        # Exit Button
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=1, column=2, padx=10)

        # Listbox to show contacts
        self.contact_listbox = tk.Listbox(root, height=15, width=60)
        self.contact_listbox.pack(pady=20)

    def add_contact(self):
        # Get contact info from entry boxes
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        # Check if name and phone are filled
        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)  # Add contact to the list
            self.clear_entries()  # Clear the input fields
            messagebox.showinfo("Success", "Contact added successfully!")  # Show success message
        else:
            messagebox.showwarning("Input Error", "Name and phone are required!")  # Warn if fields are empty

    def view_contacts(self):
        # Clear the listbox first
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            # Show contact name and phone number in listbox
            self.contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

    def search_contact(self):
        search_query = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_query:
            self.contact_listbox.delete(0, tk.END)
            found = False  # Flag to check if we found a contact
            for contact in self.contacts:
                # Check if search query matches name or phone
                if search_query.lower() in contact["Name"].lower() or search_query in contact["Phone"]:
                    self.contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")
                    found = True
            if not found:
                messagebox.showwarning("Search Result", "No contact found!")  # Alert if not found

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            new_name = simpledialog.askstring("Update Contact", f"New name (current: {contact['Name']}):")
            new_phone = simpledialog.askstring("Update Contact", f"New phone (current: {contact['Phone']}):")
            new_email = simpledialog.askstring("Update Contact", f"New email (current: {contact['Email']}):")
            new_address = simpledialog.askstring("Update Contact", f"New address (current: {contact['Address']}):")
            
            # Update only if new value is given
            if new_name:
                contact['Name'] = new_name
            if new_phone:
                contact['Phone'] = new_phone
            if new_email:
                contact['Email'] = new_email
            if new_address:
                contact['Address'] = new_address
            
            self.view_contacts()  # Refresh contact list
            messagebox.showinfo("Success", "Contact updated!")  # Show success message
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update.")  # Warn if no selection

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            del self.contacts[selected_index[0]]  # Remove selected contact
            self.view_contacts()  # Refresh contact list
            messagebox.showinfo("Success", "Contact deleted!")  # Show success message
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")  # Warn if no selection

    def clear_entries(self):
        # Clear all input fields
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

# Main function to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
