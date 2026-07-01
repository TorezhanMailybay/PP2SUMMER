from connect import connect
import csv


def add_contact():
    conn = connect()
    cur = conn.cursor()

    username = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute(
        "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
        (username, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added!")


def show_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    print("\nPhoneBook:")

    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

    cur.close()
    conn.close()


def search_contact():
    conn = connect()
    cur = conn.cursor()

    name = input("Enter name to search: ")

    cur.execute(
        "SELECT * FROM phonebook WHERE username = %s",
        (name,)
    )

    rows = cur.fetchall()

    if rows:
        print("\nFound:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    else:
        print("Contact not found.")

    cur.close()
    conn.close()


def update_contact():
    conn = connect()
    cur = conn.cursor()

    name = input("Enter contact name to update: ")

    cur.execute("SELECT * FROM phonebook WHERE username = %s", (name,))
    row = cur.fetchone()

    if row is None:
        print("Contact not found!")
        cur.close()
        conn.close()
        return

    print("1. Update name")
    print("2. Update phone")

    choice = input("Choose: ")

    if choice == "1":
        new_name = input("Enter new name: ")
        cur.execute(
            "UPDATE phonebook SET username = %s WHERE username = %s",
            (new_name, name)
        )

    elif choice == "2":
        new_phone = input("Enter new phone: ")
        cur.execute(
            "UPDATE phonebook SET phone = %s WHERE username = %s",
            (new_phone, name)
        )

    else:
        print("Invalid choice!")
        cur.close()
        conn.close()
        return

    conn.commit()
    print("Contact updated!")

    cur.close()
    conn.close()


def delete_contact():
    conn = connect()
    cur = conn.cursor()

    print("Delete by:")
    print("1. Name")
    print("2. Phone")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        cur.execute(
            "DELETE FROM phonebook WHERE username = %s",
            (name,)
        )

    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute(
            "DELETE FROM phonebook WHERE phone = %s",
            (phone,)
        )

    else:
        print("Invalid choice!")
        cur.close()
        conn.close()
        return

    conn.commit()

    if cur.rowcount > 0:
        print("Contact deleted!")
    else:
        print("Contact not found!")

    cur.close()
    conn.close()


def import_from_csv():
    conn = connect()
    cur = conn.cursor()

    filename = input("Enter CSV file name (example: contacts.csv): ")

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                cur.execute(
                    "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
                    (row[0], row[1])
                )

        conn.commit()
        print("Contacts imported successfully!")

    except FileNotFoundError:
        print("File not found!")

    cur.close()
    conn.close()


while True:
    print("\n===== PHONEBOOK =====")
    print("1. Add contact")
    print("2. Show contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Import from CSV")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        show_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        import_from_csv()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")