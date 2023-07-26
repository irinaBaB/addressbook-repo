import json

from models.contact import Contact
import random
import string
import jsonpickle
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
                               workphone=random_digits(), secondaryphone=random_digits(), email="petay@gmail.com", email2 = "test2@gmail.com", byear="1982", bmonth="April", bday="1")
             for i in range(n)

             # Contact(firstname=random_string("name", 10), address="2/3 Small street", homephone=random_digits(), mobilephone=random_digits(),
             #         workphone=random_digits(), email="petay@gmail.com", byear="1982", bmonth="April", bday="1"),
             # Contact(firstname=random_string("name",10), mobilephone=random_digits())
            ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=4)
    out.write(jsonpickle.encode(test_data))
