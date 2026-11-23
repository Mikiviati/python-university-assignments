class Sender:
    first = True

    @staticmethod
    def report(t):
        print("greettings" if t.first else "Get Away")
        t.first = False


class Asker:
    @staticmethod
    def askall(lst):
        for e in lst:
            e.report()
