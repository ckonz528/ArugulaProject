def show_list(lst):
    for recipe in lst:
        print(f"-{recipe}")


class ShowList:
    def __init__(self, lst):
        self.list = lst

    def __call__(self, lists):
        show_list(lists[self.list])


class CopyList:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def __call__(self, lists):
        lists[self.dst] = lists[self.src]


class RenameList:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def __call__(self, lists):
        lists[self.dst] = lists[self.src]
        del lists[self.src]


class ExportList:
    def __init__(self, lst):
        self.list = lst

