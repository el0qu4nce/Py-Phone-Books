import sqlite3


def add_person():
    name = input("Enter the person's name: ")
    number = input("Enter the person's phonenumber: ")
    connection = sqlite3.connect("phone_dict.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO phonenumbers VALUES (?,?)", (number, name))
    connection.commit()
    connection.close()
    print("Ready!")
    # if "Ready" message appears, the sql works!


def see_user():
    name = input("Enter the person's name: ")
    connection = sqlite3.connect("phone_dict.db")
    cursor = connection.cursor()
    rows = cursor.execute("SELECT * FROM phonenumbers").fetchall()
    for i in rows:
        if i[1] == name:
            print(f"There is {i[1]} with phonenumber {i[0]}")
            break


def get_status_code():
    status_code = int(input("Do you want to add person (1) or find person?(2)"))
    return status_code


def work_with_db(status):
    if status == 1:
        add_person()
    else:
        see_user()
