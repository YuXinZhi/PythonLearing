<<<<<<< HEAD
'''
继承

'''
class Parent:
    '''
    parent class
    '''
    parentAttr = 100
=======
class Parent:   #定义父类

    parentAttr = 100

>>>>>>> origin/master
    def __init__(self):
        print("parent's construted method")

    def parentMethod(self):
<<<<<<< HEAD
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

=======
        print("parentMehtod")

    def setAttr(self,attr):
        Parent.parentAttr=attr

    def getAttr(self):
        print("parent's attr",Parent.parentAttr)

class Child(Parent):    #定义子类
    def __init__(self):
        Parent()
        print("child's constructed method")

    def childMethod(self):
        print("childMethod")
>>>>>>> origin/master
