from crenation_utils.model.model import OrientBase

__author__ = 'lto'


class Entry(OrientBase):

    def __init__(self, name=None, port=None, ip=None):
        super(Entry, self).__init__()
        self.name = name
        self.port = port
        self.ip = ip

    def __str__(self):
        return "MyEntry [_rid=%s, name=%s ...]" % (self._rid, self.name)