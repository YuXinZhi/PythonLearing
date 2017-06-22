from demo import *
worker=Employee('mengmeng',10000)
worker.hello()
print(type(worker))

print(hasattr(Employee,'ssstr'))
print(Employee.__name__)
print(Employee.__doc__)
print(Employee.__dict__)