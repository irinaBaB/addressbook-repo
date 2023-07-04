from sys import maxsize
class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, address=None, homephone=None, mobilephone=None,
                 email=None, byear=None, bmonth=None, bday=None, idc=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.email = email
        self.byear = byear
        self.bmonth = bmonth
        self.bday = bday
        self.idc = idc

    def __repr__(self):
        return "%s:%s:%s" % (self.idc, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.idc is None or other.idc is None or self.idc == other.idc) or self.lastname == other.lastname or self.firstname == other.firstname

    def id_or_max(self):
        if self.idc:
            return int(self.idc)
        else:
            return maxsize
