# define city properties 
import pprint
pp = pprint.PrettyPrinter(indent=4)
from geopy import distance

# get distance with Geopy
def get_distance(x,y):
	#dc_cord = get_lat_lon(dep_city) 
	#tc_cord = get_lat_lon(term_city)
	return distance.great_circle(x,y).km

class Grid(object):
	def __init__(self, lat, lon, we, le):
		self._lat = lat
		self._lon = lon
		self._workeff = we
		self._lateff = le

	@property
	def lat(self):
		return self._lat
	@property
	def lon(self):
		return self._lon
	@property
	def workeff(self):
		return self._workeff
	@property
	def lateff(self):
		return self._lateff

	def reset_workeff(self,worke):
		self._workeff2 = worke
	def reset_lateff(self,late):
		self._lateff2 = late
	@property
	def lateff2(self):
		return self._lateff2*2	
	@property
	def workeff2(self):
		return self._workeff2*8
	def _get_score(self):
		return self.workeff2+self.lateff2
	@property
	def score(self):
		return self._get_score()		
	def printout(self):
		pp.pprint((self.lat,self.lon,self.score))

class City(object):
	def __init__(self,name,lat,lon,cpi,gdp,cri,cro):
		self._name = name
		self._lat = lat
		self._lon = lon
		self._cpi = cpi
		self._gdp = gdp
		self._cri = cri
		self._cro = cro
	@property
	def name(self):
		return self._name
	@property
	def cpi(self):
		return self._cpi/10
	@property
	def gdp(self):
		return 10000/self._gdp
	@property
	def cri(self):
		return self._cri/10
	@property
	def cro(self):
		return self._cro/10

	def cal_fee(self,pdata):
	    des = (self._lat,self._lon)
	    total = 0
	    for each in pdata:
	        cord = (float(each.split(',')[0]),float(each.split(',')[1]))
	        #print(des,cord)
	        dist = get_distance(des,cord)
	        fee = 0.2771 * dist
	        total += fee
	    self._fee = total

	@property
	def fee(self):
		return self._fee/1000

	def get_vector(self):
		return [self.cpi,self.gdp,self.cri,self.cro,self.fee]
	
	def printout(self):
		pp.pprint((self.name,self.cpi,self.gdp,self.cri,self.cro,self.fee))

	
	

	
	
	


	
	

	
	
	