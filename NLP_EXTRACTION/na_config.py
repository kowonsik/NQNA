# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 00:08:46 2015

@author: deokwooj
"""
"""
* Description 
- This file defines constant values shared among python modules.
- Should be included all python modules first. 
"""

# Loading common python modules to be used. 
import os
import sys, traceback
import numpy as np
from numpy.linalg import inv
from numpy.linalg import norm
import uuid
import pylab as pl
from scipy import signal
from scipy import stats
from scipy import sparse
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from multiprocessing import Pool
#from datetime import datetime
import datetime as dt
from dateutil import tz
import shlex, subprocess
import time
import itertools
import calendar
import random
from matplotlib.collections import LineCollection
import pprint
import warnings
import data_tools as nt
from na_const import * 

# dictionary file path
DICT_ID_NAME = "./binfiles/dict_id_name.p"
DICT_ORG = "./binfiles/dict_org.p"
DICT_TYPE = "./binfiles/dict_type.p"
DICT_POS = "./binfiles/dict_pos.p"
DICT_CODE = "./binfiles/dict_code.p"
DICT_CLASSIFIED = "./binfiles/dict_classified.p"
DICT_INFORMER = "./binfiles/dict_informer.p"

DICT_ORG_SET = "./binfiles/dict_org_set.p"
DICT_POS_SET = "./binfiles/dict_pos_set.p"

DICT_E_INFORMER_SET = "./binfiles/dict_e_informer_set.p"

DICT_NOUNS = "./binfiles/nouns.p"

DICT_ARTICLE_ID_SET = "./binfiles/dict_article_id_set.p"
DICT_N_INFORMER_SET = "./binfiles/dict_n_informer_set.p"

DICT_SPLIT_ARR_NOUNS = "./binfiles/dict_split_arr_nouns.p"

# news info tuple in extraction sheet of reference.xlsx
DICT_NEWS_INFO = "./binfiles/dict_news_info.p"

####
#
NEWS_SRC_OBJ="./binfiles/NewsSrcObjs.p" 
NEWS_QUO_OBJ="./binfiles/NewsQuoObjs.p"
ANAL_MAT_OBJ="./binfiles/AnalMatObj.p"
QUO_CLUSTER_OBJ="./binfiles/quo_cluster.p"
DUMP_OBJ="./binfiles/dump.p"


# Excel file inputs
#REFERENCE_EXCEL = "./exlfiles/reference.xlsx"
REFERENCE_EXCEL = "./exlfiles/reference_3.xlsx"
EXTRACTION_SHEET = "extraction" 

WHOLETABLE_EXCEL = './exlfiles/wholetable.xlsx'
WHOLETABLE_SHEET = 'wholetable'

