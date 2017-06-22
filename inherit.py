class Parent:   #定义父类

    parentAttr = 100

    def __init__(self):
        print("parent's construted method")

    def parentMethod(self):
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