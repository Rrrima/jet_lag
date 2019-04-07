
from math import sin,pi
import scipy.integrate
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class DailyEff(object):
	def __init__(self, day, delta):
		A = 0.5
		B = 1
		delta_r = abs(delta) - day*B
		if delta_r < 0:
			delta_r = 0
		self._alpha = 1 - A * sin(pi*delta_r/24)
		self._start = delta + 8
		self._end = delta + 20
	def f(self,x):
		a = self._alpha
		if x>=-4 and x<-1:
			return -a/8*(x+1)
		elif x>=-1 and x<=6:
			return 0
		elif x>6 and x<10:
			return a/4*(x-6)
		elif x>=10 and x<=15:
			return a
		elif x>15 and x<23:
			return -a/8*(x-23)
		elif x>=23 and x<=30:
			return 0
		elif x>30 and x<=32:
			return a/4*(x-30)
	def cal_eff(self):
		s = self._start
		e = self._end
		return scipy.integrate.quad(self.f, s, e)

def lat_eff(delta):
	return 1-0.2*abs(delta)/180


def get_lon_range(arr):
	x = [float(arr[i].split(',')[1]) for i in range(len(arr))]
	return [min(x),max(x)]

def get_lat_range(arr):
	x = [float(arr[i].split(',')[0]) for i in range(len(arr))]
	return [min(x),max(x)]

def init_arr(x):
	a = []
	for i in range(x):
		a.append([])
	return a

def generate_attr(data,arr):
	lenx = len(data)
	result = init_arr(lenx)
	i = 0
	if arr == 'workeff':
		for eachline in data:
			for each in eachline:
				result[i].append(each.workeff2) 
			i+=1
	elif arr == 'lateff':
		for eachlline in data:
			for each in eachline:
				result[i].append(each.lateff2)
			i+=1
	elif arr == 'score':
		for eachline in data:
			for each in eachline:
				result[i].append(each.score)
			i+=1
	return result


def draw_heatmap(data):
	sns.set()
	sns.heatmap(data,cmap='GnBu',linewidths=.3)
	plt.show()


def get_entropy(data0):
	n,m = np.shape(data0)
	maxium=np.max(data0,axis=0)
	minium=np.min(data0,axis=0)
	data= (data0-minium)*1.0/(maxium-minium)
	sumzb=np.sum(data,axis=0)
	a=data*1.0
	a[np.where(data==0)]=0.0001
	e=(-1.0/np.log(n))*np.sum(data*np.log(a),axis=0)
	w=(1-e)/np.sum(1-e)
	recodes=np.sum(data*w,axis=1)
	return recodes


def draw_barth(names,data):
	sns.barplot(names, data, palette="GnBu", orient="v")
	plt.ylabel('comprehensive score')
	sns.despine(bottom=True)
	plt.show()







   