# this is used for testing unknown-funcs
from sympy import *
import scipy.integrate
from utils import *
import numpy as np
def f(alpha,x):
	if x<5:
		return x
	else:
		return alpha-x

import matplotlib.pyplot as plt
import seaborn as sns
