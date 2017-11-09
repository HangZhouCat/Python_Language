'''

高阶函数测试代码

'''

def Incoming_Parameters(x, y, f):
    '''

    传入参数代码测试

一个函数能能接收另一个函数作为参数，这种函数就称之为高阶函数。
    :return:
    '''

    return f(x) + f(y)

    pass

def Main():
    print(abs(-10))  # abs(-10)是函数调用
    print(abs)  # abs是函数本身

    f = abs         #将函数本身赋值给变量
    print(f)       #函数本身可以赋值给变量，即变量可以指向函数

    print(f(-10))    #验证上述结论

    '''
    
    那么函数名其实就是指向函数的变量！
    
    '''


    print(Incoming_Parameters(-5, 6, abs))      #传入参数代码测试

if __name__ == '__main__':
    Main()


