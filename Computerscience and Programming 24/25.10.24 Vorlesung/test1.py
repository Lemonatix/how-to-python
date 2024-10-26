class Element:
    def __init__(self, massArgument, nameArgument):
        self.mass = massArgument
        self.name = nameArgument
        d = Element("Wrongium", -3) # does not generate error as expected
