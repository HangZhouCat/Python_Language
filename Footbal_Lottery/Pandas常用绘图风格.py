import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as  pd

def dr_xtyp(_dat):
    for xss in plt.style.available:
        plt.style.use(xss)
        print(xss)
        _dat['Open'].plot()
        _dat['Close'].plot()
        _dat['High'].plot()
        _dat['Low'].plot()
        fss = 'tmp/stk001_' + xss + '_pd.png'
        plt.savefig(fss)
        plt.show()

def Main():
    df = pd.read_csv('dat/appl2014.csv', index_col=0, parse_dates=[0], encoding='gbk')
    d30 = df[:30]
    dr_xtyp(d30)

if __name__ == '__main__':
    Main()
