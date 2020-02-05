class t(object):
    def __init__(self):
        self.next = None

if __name__ == "__main__":
    a = t()
    b = t()
    a.next = b
    c = a
    while c.next != None:
        c = c.next
    c.next = a
    pass