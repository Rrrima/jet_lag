
from geopy.geocoders import Nominatim
from geopy import distance
from math import sin,pi
import scipy.integrate


def get_cityname(cityname):
	return (lat,lon)

# get distance with Geopy
def get_distance_by_latlon(dep_city,term_city):
	#dc_cord = get_lat_lon(dep_city) 
	#tc_cord = get_lat_lon(term_city)
	return distance.great_circle(dc_cord,tc_cord).km

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







   