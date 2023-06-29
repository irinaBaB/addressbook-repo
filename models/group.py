
class Group:
    def __init__(self, name=None, header=None, footer=None, idg=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.idg = idg

    def __repr__(self):
       return "%s:%s" % (self.idg, self.name)

    def __eq__(self, other):
        return self.idg == other.idg and self.name == other.name


