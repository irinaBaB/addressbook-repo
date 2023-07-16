from models.group import Group
import random
import string
import jsonpickle
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def randon_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(name="", header="", footer="")] + [
    Group(name=randon_string("name", 8), header=randon_string("header", 7), footer=randon_string("footer", 5))
    for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=4)
    out.write(jsonpickle.encode(test_data))
    #out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
