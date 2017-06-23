'''
继承

'''
class Parent:
    '''
    parent class
    '''
    parentAttr = 100
    def __init__(self):
        print("parent's construted method")

    def parentMethod(self):
        print("parent's method")

    def setAttr(self, attr):
        Parent.parentAttr=attr

    def getAttr(self):
        print("parent.attr",Parent.parentAttr)
        return Parent.parentAttr

class Child:
    '''
    child class
    '''
    def __init__(self):
        print("child's constructed method")

    def childMethod():

