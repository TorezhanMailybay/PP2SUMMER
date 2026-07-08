from connect import connect
import csv


def add_or_update_contact():
    conn = connect()
    cur = conn.cursor()

    username = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute(
        "CALL upsert_contact(%s, %s)",
        (username, phone)
    )

    conn.commit()

    cur.close()
    conn.close()

    print("Contact added or updated!")


def show_contacts():
    conn = connect()
    cur = conn.cursor()

    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    cur.execute(
        "SELECT * FROM get_contacts(%s, %s)",
        (limit, offset)
    )

    rows = cur.fetchall()

    if rows:
        print("\nPhoneBook:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    else:
        print("No contacts found.")

    cur.close()
    conn.close()


def search_contact():
    conn = connect()
    cur = conn.cursor()

    pattern = input("Enter name or phone: ")

    cur.execute(
        "SELECT * FROM search_contacts(%s)",
        (pattern,)
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


def delete_contact():
    conn = connect()
    cur = conn.cursor()

    value = input("Enter username or phone: ")

    cur.execute(
        "CALL delete_contact(%s)",
        (value,)
    )

    conn.commit()

    print("Contact deleted.")

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
                    "CALL upsert_contact(%s, %s)",
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
    print("1. Add / Update contact")
    print("2. Show contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Import from CSV")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_or_update_contact()

    elif choice == "2":
        show_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        import_from_csv()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")