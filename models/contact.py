from sys import maxsize
class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, address=None, homephone=None, mobilephone=None,
                 workphone=None, secondaryphone=None, email=None, email2=None, email3=None, byear=None, bmonth=None, bday=None,
                 id=None, all_phones_from_home_page=None, group_name=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.byear = byear
        self.bmonth = bmonth
        self.bday = bday
        self.id = id
        self.group_name = group_name
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.email)

    def __eq__(self, other):
        # return (self.id is None or other.id is None or self.id == other.id) or self.lastname == other.lastname or self.firstname == other.firstname
        return (self.id is None or other.id is None or self.id == other.id)\
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
