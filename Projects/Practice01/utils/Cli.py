from dao.Contact import *


def show():
    print("==============================\n"
          "📇 Welcome to Contact Manager\n"
          "==============================")
    print(
        "Please choose an option:\n"
        "1. ➕ Add a new contact\n"
        "2. 🗑️ Delete a contact\n"
        "3. ✏️ Update a contact\n"
        "4. 🔍 Get contact details\n"
        "5. 📖 Show all contacts\n"
        "6. ❌ Exit\n"
    )


def add_contact():
    name = input("Enter a name: ").strip()
    phone = input("Enter a phone number: ").strip()
    email = input("Enter an email: ").strip()
    address = input("Enter an address (optional): ").strip()

    contact = Contact(
        cid=0,
        name=name,
        phoneNo=phone,
        email=email,
        address=address
    )
    print(f"✅ Contact '{contact.name}' added successfully!\n")
    return contact


def delete_contact():
    cid = input("🗑️ Enter the ID of the contact to delete: ").strip()
    if not cid.isdigit():
        print("❌ Please enter a valid numeric contact ID!")
        return None

    confirmation = input(f"⚠️ Are you sure you want to delete contact #{cid}? (y/n): ").strip().lower()
    if confirmation == "y":
        print(f"✅ Contact #{cid} deleted successfully!\n")
        return int(cid)
    else:
        print("❌ Deletion cancelled.\n")
        return None


def update_contact(contact_list):
    cid_input = input("✏️ Enter the ID of the contact to update: ").strip()
    if not cid_input.isdigit():
        print("❌ Invalid contact ID!")
        return None
    cid = int(cid_input)

    contact = next((c for c in contact_list if c.cid == cid), None)
    if contact is None:
        print(f"❌ No contact found with ID {cid}.")
        return None

    # Show existing contact
    print("\nCurrent Contact Details:")
    print(contact)
    print("\nPress Enter to keep existing value:")

    # Get new data
    new_name = input(f"Name [{contact.name}]: ").strip()
    new_phone = input(f"Phone [{contact.phoneNo}]: ").strip()
    new_email = input(f"Email [{contact.email}]: ").strip()
    new_address = input(f"Address [{contact.address}]: ").strip()

    # Only update if new value is provided
    if new_name:
        contact.name = new_name
    if new_phone:
        contact.phoneNo = new_phone
    if new_email:
        contact.email = new_email
    if new_address:
        contact.address = new_address

    print(f"\n✅ Contact ID {cid} updated successfully!")
    return contact


def get_contact_details(contact_list):
    cid_input = input("🔍 Enter the ID of the contact you want to view: ").strip()
    if not cid_input.isdigit():
        print("❌ Invalid contact ID!")
        return None

    cid = int(cid_input)

    # Search for the contact
    contact = next((c for c in contact_list if c.cid == cid), None)
    if contact is None:
        print(f"❌ No contact found with ID {cid}.")

    print(contact)


def show_all_contacts(contact_list):
    if not contact_list:
        print("📖 No contacts available!")
        return

    print("\n📖 Contact List:")
    print("=" * 50)
    for contact in contact_list:
        print(contact)  # Uses Contact's __str__ method
    print("=" * 50)
