import sqlite3

# Function to create table (only runs once)
def create_table():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL, 
                   phone TEXT NOT NULL UNIQUE,
                   email TEXT
    )
    """)
    conn.commit()
    conn.close()

# Function to add a contact
def add_contact():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    name = input("Enter the name: ")
    phone = input("Enter the phone: ")
    email = input("Enter the email: ")

    try:
        cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        conn.commit()
        print("✅ Contact added successfully!")
    except sqlite3.IntegrityError:
        print("⚠️ A contact with this phone number already exists.")
    
    conn.close()

# Function to view contacts
def view_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()

    print("\n-- Saved Contacts --")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")

    conn.close()

# Main menu loop
def main():
    create_table()
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, please try again.")

# Run program
if __name__ == "__main__":
    main()
