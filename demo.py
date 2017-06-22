class Employee:
    classstr="employee"
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay

    def hello(self):
        '''
        say hello
        :return:
        '''
        print(self.name)
        print("say hello")


