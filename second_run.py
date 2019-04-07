from utils import *
from data import *
from city import City
import pprint
import math
pp = pprint.PrettyPrinter(indent=4)

def  generate_matrix(data):
	return [each.get_vector() for each in data]
		
pdata = participants_data() # (lat,lon)
citydata = city_data()
for each in citydata:
	each.cal_fee(pdata)

matrix = generate_matrix(citydata)
print(matrix)
result = get_entropy(matrix)
final = [math.pow(100,-x)*100 for x in result]
names = [eachcity.name for eachcity in citydata]
draw_barth(names,final)

