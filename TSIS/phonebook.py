from connect import connect
import csv
import json


def add_contact():
    conn = connect()
    cur = conn.cursor()

    username = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    group = input("Group (Family/Work/Friend/Other): ")
    phone = input("Phone: ")
    phone_type = input("Phone type (home/work/mobile): ")

    cur.execute(
        "CALL add_contact(%s,%s,%s,%s,%s,%s)",
        (username, email, birthday, group, phone, phone_type)
    )

    conn.commit()

    cur.close()
    conn.close()

    print("Contact added!")


def show_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            c.username,
            c.email,
            c.birthday,
            g.name,
            p.phone,
            p.type
        FROM contacts c
        LEFT JOIN groups g
            ON c.group_id=g.id
        LEFT JOIN phones p
            ON c.id=p.contact_id
        ORDER BY c.username
    """)

    rows = cur.fetchall()

    print()

    for row in rows:
        print(f"""
Name: {row[0]}
Email: {row[1]}
Birthday: {row[2]}
Group: {row[3]}
Phone: {row[4]}
Type: {row[5]}
-----------------------------
""")

    cur.close()
    conn.close()


def search_contact():
    conn = connect()
    cur = conn.cursor()

    query = input("Search: ")

    cur.execute(
        "SELECT * FROM search_contacts(%s)",
        (query,)
    )

    rows = cur.fetchall()

    if rows:

        print()

        for row in rows:
            print(f"""
Name: {row[1]}
Email: {row[2]}
Birthday: {row[3]}
Group: {row[4]}
Phone: {row[5]}
Type: {row[6]}
-----------------------------
""")

    else:
        print("Nothing found.")

    cur.close()
    conn.close()

def filter_by_group():
    conn = connect()
    cur = conn.cursor()

    group = input("Enter group: ")

    cur.execute("""
        SELECT
            c.username,
            c.email,
            c.birthday,
            g.name,
            p.phone,
            p.type
        FROM contacts c
        JOIN groups g
            ON c.group_id = g.id
        LEFT JOIN phones p
            ON c.id = p.contact_id
        WHERE g.name = %s
    """, (group,))

    rows = cur.fetchall()

    if rows:
        print()
        for row in rows:
            print(f"""
Name: {row[0]}
Email: {row[1]}
Birthday: {row[2]}
Group: {row[3]}
Phone: {row[4]}
Type: {row[5]}
-----------------------------
""")
    else:
        print("No contacts found.")

    cur.close()
    conn.close()


def sort_contacts():
    conn = connect()
    cur = conn.cursor()

    print("1. Name")
    print("2. Birthday")

    choice = input("Choose: ")

    if choice == "1":
        order = "c.username"
    elif choice == "2":
        order = "c.birthday"
    else:
        print("Invalid choice.")
        cur.close()
        conn.close()
        return

    cur.execute(f"""
        SELECT
            c.username,
            c.email,
            c.birthday,
            g.name,
            p.phone,
            p.type
        FROM contacts c
        LEFT JOIN groups g
            ON c.group_id = g.id
        LEFT JOIN phones p
            ON c.id = p.contact_id
        ORDER BY {order}
    """)

    rows = cur.fetchall()

    for row in rows:
        print(f"""
Name: {row[0]}
Email: {row[1]}
Birthday: {row[2]}
Group: {row[3]}
Phone: {row[4]}
Type: {row[5]}
-----------------------------
""")

    cur.close()
    conn.close()


def add_phone():
    conn = connect()
    cur = conn.cursor()

    username = input("Contact name: ")
    phone = input("New phone: ")
    phone_type = input("Type (home/work/mobile): ")

    cur.execute(
        "CALL add_phone(%s,%s,%s)",
        (username, phone, phone_type)
    )

    conn.commit()

    cur.close()
    conn.close()

    print("Phone added.")


def move_to_group():
    conn = connect()
    cur = conn.cursor()

    username = input("Contact name: ")
    group = input("New group: ")

    cur.execute(
        "CALL move_to_group(%s,%s)",
        (username, group)
    )

    conn.commit()

    cur.close()
    conn.close()

    print("Contact moved.")

def export_to_json():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            c.username,
            c.email,
            c.birthday,
            g.name,
            p.phone,
            p.type
        FROM contacts c
        LEFT JOIN groups g
            ON c.group_id = g.id
        LEFT JOIN phones p
            ON c.id = p.contact_id
    """)

    rows = cur.fetchall()

    contacts = []

    for row in rows:
        contacts.append({
            "username": row[0],
            "email": row[1],
            "birthday": str(row[2]),
            "group": row[3],
            "phone": row[4],
            "type": row[5]
        })

    with open("contacts.json", "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)

    cur.close()
    conn.close()

    print("Export completed!")


def import_from_json():
    conn = connect()
    cur = conn.cursor()

    filename = input("JSON file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            contacts = json.load(file)

        for contact in contacts:
            cur.execute(
                "CALL add_contact(%s,%s,%s,%s,%s,%s)",
                (
                    contact["username"],
                    contact["email"],
                    contact["birthday"],
                    contact["group"],
                    contact["phone"],
                    contact["type"]
                )
            )

        conn.commit()
        print("Import completed!")

    except FileNotFoundError:
        print("File not found.")

    cur.close()
    conn.close()

def import_from_csv():
    conn = connect()
    cur = conn.cursor()

    filename = input("CSV file name: ")

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                cur.execute(
                    "CALL add_contact(%s,%s,%s,%s,%s,%s)",
                    (
                        row["username"],
                        row["email"],
                        row["birthday"],
                        row["group"],
                        row["phone"],
                        row["type"]
                    )
                )

        conn.commit()
        print("Import completed!")

    except FileNotFoundError:
        print("File not found.")

    cur.close()
    conn.close()


while True:

    print("\n========= PHONEBOOK =========")

    print("1. Add contact")
    print("2. Show contacts")
    print("3. Search")
    print("4. Filter by group")
    print("5. Sort contacts")
    print("6. Add second phone")
    print("7. Move to group")
    print("8. Import from CSV")
    print("9. Export to JSON")
    print("10. Import from JSON")
    print("11. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        show_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        filter_by_group()

    elif choice == "5":
        sort_contacts()

    elif choice == "6":
        add_phone()

    elif choice == "7":
        move_to_group()

    elif choice == "8":
        import_from_csv()

    elif choice == "9":
        export_to_json()

    elif choice == "10":
        import_from_json()

    elif choice == "11":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
    