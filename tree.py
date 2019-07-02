class Tree:
    def __init__(self):
        self._name = None
        self._left = None
        self._right = None
    def name(self):
        return self._name
    def left(self):
        return self._left
    def right(self):
        return self._right
    def is_leaf(self):
        return self._left == None and self._right == None
    def __str__(self):
        if self.is_leaf():
            return str(self.name())
        else:
            return "({}, {})".format(str(self.left()), str(self.right()))
    #def __eq__(self, other):
        #return self._name == other._name and self._left == other._left \
               #and self._right == other._right