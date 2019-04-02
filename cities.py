# define city properties 
from data import get_timezone
from datetime import datetime
from pytz import timezone
import pytz
def convert_to_utc(timezone):
	cur_tz = pytz.timezone(timezone) 
	utc = pytz.utc

class city(object):
	def __init__(self, lat, lon, name):
		self._name = name
		self._lat = lat
		self._lon = lon
		self._timezone = get_timezone(str(self._lat)+str(self._lon))
		self._offset = convert_to_utc(self._timezone)
