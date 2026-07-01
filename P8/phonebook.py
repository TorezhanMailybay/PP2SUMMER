from connect import connect


def add_or_update_contact():
    conn = connect()
    cur = conn.cursor()

    username = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute("CALL upsert_contact(%s, %s)", (username, phone))

    conn.commit()

    cur.close()
    conn.close()

    print("Done!")


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

    print()

    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

    cur.close()
    conn.close()


def search_contact():
    conn = connect()
    cur = conn.cursor()

    pattern = input("Search: ")

    cur.execute(
        "SELECT * FROM search_contacts(%s)",
        (pattern,)
    )

    rows = cur.fetchall()

    if rows:
        print()

        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

    else:
        print("Nothing found.")

    cur.close()
    conn.close()


def delete_contact():
    conn = connect()
    cur = conn.cursor()

    value = input("Enter username or phone: ")

    cur.execute("CALL delete_contact(%s)", (value,))

    conn.commit()

    cur.close()
    conn.close()

    print("Deleted!")


while True:
    print("\n===== PHONEBOOK =====")
    print("1. Add / Update contact")
    print("2. Show contacts")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")

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
        break

    else:
        print("Invalid choice!")