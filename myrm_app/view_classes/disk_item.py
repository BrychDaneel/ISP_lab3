class DiskItem(object):
    name = None
    is_dir = None
    is_removed = None
    remove_date = None
    path=None

    def __init__(self, name, is_dir=False, 
                 is_removed=False, remove_date=None, path=None):
        self.name = name
        self.is_dir = is_dir
        self.is_removed = is_removed
        self.remove_date = remove_date
        self.path = path
