import os
import re
import pandas as pd
import numpy as np
import arrow
import datetime

import requests
import bs4
from bs4 import BeautifulSoup

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.colors
from matplotlib import cm


rs0 = '/tfbData/'
fgid, fdat = rs0 + 'gid2017.dat', rs0 + 'xdat2017.dat'
tim0 = arrow.now()
