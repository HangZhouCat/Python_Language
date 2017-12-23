import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as  pd

def dr_xtyp(_dat):
    for xss in plt.style.available:
        plt.style.use(xss)
        print(xss)
        plt.plot(_dat['Open'])
        plt.plot(_dat['Close'])
        plt.plot(_dat['High'])
        plt.plot(_dat['Low'])
        fss = 'tmp/stk001_' + xss + '.png'
        plt.savefig(fss)
        plt.show()

def Main():
    df = pd.read_csv('dat/appl2014.csv', index_col=0, parse_dates=[0], encoding='gbk')
    d30 = df[:30]
    dr_xtyp(d30)

if __name__ == '__main__':
    Main()
