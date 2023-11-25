import sqlite3

func = int(input("Do you want to add person (1) or find person?(2)"))
if func == 1:
    name = input("Enter the person's name: ")
    number = input("Enter the person's phonenumber: ")
    connection = sqlite3.connect("phone_dict.db")
    cursor = connection.cursor()
    params = (number, name)
    cursor.execute(f"INSERT INTO phonenumbers VALUES ({number}, {name})")
    connection.commit()
    connection.close()
    print("Ready!")
else:
    name = input("Enter the person's name: ")
    connection = sqlite3.connect("phone_dict.db")
    cursor = connection.cursor()
    rows = cursor.execute("SELECT * FROM phonenumbers").fetchall()
    for i in rows:
        if i[0] == name:
            print(f"There is {i[1]} with phonenumber {i[0]}")
            break
