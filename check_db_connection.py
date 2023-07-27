import pymysql

from fixture.orm import ORMFixture
from models.group import Group
from models.contact import Contact

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


try:
    l = db.get_contacts_not_in_group(Group(id='445'))
    for item in l:
        print(item)
        print(len(l))
finally:
   pass #db.destroy()





#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")




# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()