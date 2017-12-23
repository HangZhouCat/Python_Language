import os
import re
import pandas as pd
import numpy as np
import arrow
import datetime

import requests
import bs4
from bs4 import BeautifulSoup
from robobrowser import RoboBrowser

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.colors
from matplotlib import cm

import zsys
import ztools as zt
import zpd_talib as zta
#
import tfb_sys as tfsys
import tfb_tools as tft


rs0 = '/tfbData/'
fgid, fdat = rs0 + 'gid2017.dat', rs0 + 'xdat2017.dat'
tim0 = arrow.now()

gids = pd.read_csv(fgid,index_col=False, dtype=str, encoding='gb18030')
tim2 = arrow.now()
t1 =
