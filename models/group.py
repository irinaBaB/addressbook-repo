from sys import maxsize
class Group:
    def __init__(self, name=None, header=None, footer=None, idg=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.idg = idg

    def __repr__(self):
       return "%s:%s:%s:%s" % (self.idg, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.idg is None or other.idg is None or self.idg == other.idg) \
               and (self.name is None or other.name is None or self.name == other.name) \
               and (self.footer is None or other.footer is None or self.footer == other.name)

    def id_or_max(self):
        if self.idg:
            return int(self.idg)
        else:
            return maxsize


