#!/usr/bin/env python

import time
import datetime
import math
import csv
import random
import string
import numpy as np
import pandas as pd
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import MySQLdb

from train import art_train
from test import art_test

#train_data = pd.read_csv('sample-data/train-example.csv').to_numpy()
#test_data = pd.read_csv('sample-data/test-example.csv').to_numpy()
#x = train_data[:,1:3]
#y = test_data[:,1:3]

x = pd.read_csv('sample-data/xor_train.csv').to_numpy()
x = x[:,0:2]

r = 0.9
Tmatrix = art_train(x,rho=r) #,beta=0.000001,alpha=1.0,nep=1)
print Tmatrix
#T = art_test(y,Tmatrix,rho=r) #,beta=0.000001,alpha=1.0,nep=1)
#print T
