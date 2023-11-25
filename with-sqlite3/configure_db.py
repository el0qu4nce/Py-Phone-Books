""""
you should have "phone_dict.db" file already created, but empty inside
further we will configure lines and columns of it
"""
import sqlite3

connection = sqlite3.connect("phone_dict.db")
cursor = connection.cursor()

# making table "phonumbers" in "phone_dict.db"
cursor.execute("CREATE TABLE phonenumbers (phonenumber TEXT, name TEXT)")
