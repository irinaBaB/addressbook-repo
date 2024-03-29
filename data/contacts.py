from models.contact import Contact
import random
import string
import jsonpickle
import os.path
import getopt
import sys

const_data = [
     Contact(firstname="Petr", middlename="sergeevich", lastname="Ivanov", nickname="petya", address="2/3 Small street", homephone="089-56-67", mobilephone="997-89-706",
                       workphone="042547896", secondaryphone="(042)547896", email="petay@gmail.com", byear="1982", bmonth="April", bday="1"),
     Contact(firstname="Petr", address="2/3 Small street", homephone="089-56-67", mobilephone="997-89-706",
             workphone="042547896", email="petay@gmail.com", byear="1982", bmonth="April", bday="1"),
     Contact(firstname="Petr", mobilephone="997-89-706")
]




def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    random.choice(symbols)
    return prefix + " ".join([random.choice(symbols) for x in range(random.randrange(maxlen))])


def random_digits():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6] == '000' or n[6] == n[7] == n[8] == n[9]:
        n = str(random.randint(10 ** 9, 10 ** 10 - 1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]


test_data = [
             Contact(firstname=random_string("name",10), middlename=random_string("middlename",8), lastname=random_string('lastname',9), nickname=random_string('nickname',8), address=random_string("address",10), homephone=random_digits(), mobilephone=random_digits(),
                               workphone=random_digits(), secondaryphone=random_digits(), email="petay@gmail.com", byear="1982", bmonth="April", bday="1"),
             Contact(firstname=random_string("name", 10), address="2/3 Small street", homephone=random_digits(), mobilephone=random_digits(),
                     workphone=random_digits(), email="petay@gmail.com", byear="1982", bmonth="April", bday="1"),
             Contact(firstname=random_string("name",10), mobilephone=random_digits())
            ]
