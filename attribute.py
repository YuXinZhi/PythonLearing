from  demo import *
'''
内置类属性
'''
print(Employee.__name__)    #类名
print(Employee.__doc__)     #类的文档字符串
print(Employee.__dict__)    #类的属性（包含一个字典，由累的数据属性组成）
print(Employee.__module__)  #类定义所在的模块（类的全名是‘__main__.className’，
                            # 如果类位于一个导入模块mymod中，那么className.__main__等于mymod）
'''
{'__module__': 'demo',
 '__doc__': '\n    doc\n    ',
 'classstr': 'employee',
 '__init__': <function Employee.__init__ at 0x00000000028D07B8>,
 'hello': <function Employee.hello at 0x00000000028D0840>,
 '__dict__': <attribute '__dict__' of 'Employee' objects>,
 '__weakref__': <attribute '__weakref__' of 'Employee' objects>}
'''
print(Employee.__bases__)   #类的所有父类构成元素（包含了一个以由所有父类的元组）
