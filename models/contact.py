from sys import maxsize
class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, address=None, homephone=None, mobilephone=None,
                 workphone=None, secondaryphone=None, email=None, byear=None, bmonth=None, bday=None, idc=None, all_phones_from_home_page=None):
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
        self.byear = byear
        self.bmonth = bmonth
        self.bday = bday
        self.idc = idc
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.idc, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.idc is None or other.idc is None or self.idc == other.idc)\
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               and self.firstname == other.firstname

    def id_or_max(self):
        if self.idc:
            return int(self.idc)
        else:
            return maxsize
