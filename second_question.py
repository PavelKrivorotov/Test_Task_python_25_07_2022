

class MyElem():
    def __init__(self, val):
        self.next = None
        self.val = val

class MyQueue():
    def __init__(self, val):
        elem = MyElem(val)
        self.root = elem
        self.end = elem

    def add_elem(self, val):
        elem = MyElem(val)
        self.end.next = elem
        self.end = elem

    def get_elem(self):
        try:
            val = self.root.val
            self.root = self.root.next
        except AttributeError:
            return None
        return val


a = MyQueue(10)
a.add_elem(9)
print(a.get_elem())
print(a.get_elem())
print(a.get_elem())