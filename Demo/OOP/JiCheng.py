'''

Python面向对象中的继承 测试学习代码

'''
class Animals:
    def chi(self):
        print(self.name , '吃')
    def he(self):
        print(self.name , '喝')

class Cat:

    def __init__(self,name):
        self.name = name


    def jiao(self):
        print('喵')

class Dog(Animals):
    def __init__(self,name):
        self.name = name
    def jiao(self):
        print(self.name,'汪')

alex = Dog('李杰')
alex.jiao()


'''
以上是单继承
'''



'''

下面是多继承

'''

class Uncle:
    def du(self):
        print('赌')

    def piao(self):
        print('111111')