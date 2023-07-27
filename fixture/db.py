import pymysql
from models.group import Group
from models.contact import Contact

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self. connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select group_id,group_name,group_header,group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_in_group_list(self):
        cursor = self.connection.cursor()
        list = [ ]
        try:
            cursor.execute("select id, group_id  from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list.append(Group(id=str(id), group_id=group_id))
        finally:
            cursor.close()
        return list

    def get_group_name(self, name):
        cursor = self.connection.cursor()
        list_name = []
        try:
           cursor.execute(f"select group_name from group_list where group_name='{name}'")
           for row in cursor:
               name = row
               list_name.append(Group(name=name))
        finally:
            cursor.close()
        return list_name

    def get_contact_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select id, firstname, lastname, email, email2  from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, email, email2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, email=email, email2=email2))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
