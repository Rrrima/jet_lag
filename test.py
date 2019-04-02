from utils import *
from data import *
import pprint
pp = pprint.PrettyPrinter(indent=4)

def cal_work_eff(x,y,pdata):
	
	des = str(y)+','+str(x)
	total = 0
	result_matrix = []
	for each in pdata:
		delta = tz_delta(each,des)
		if delta<-12:
			delta = delta+24
		if delta>12:
			delta = delta-24
		#print(delta)
		cur_eff = [DailyEff(day,delta).cal_eff()[0] for day in range(3)]
		result_matrix.append(cur_eff)
		sum_eff = sum(cur_eff)
		total += sum_eff
	return {
	 'matrix': result_matrix,
	 'result':total
	}


def cal_lat_eff(x,pdata):
	total = 0
	result_matrix = []
	for each in pdata:
		delta = float(each.split(',')[0])-x
		sum_eff = lat_eff(delta)
		result_matrix.append(sum_eff)
		total += sum_eff
	return {
	 'matrix': result_matrix,
	 'result':total
	}


# main

pdata = participants_data()
range_of_lon = get_lon_range(pdata)
range_of_lat = get_lat_range(pdata)

lon = range_of_lon[0]
slat = range_of_lat[0]
lat = slat
elon = range_of_lon[1]
elat = range_of_lat[1]
result = []
i = 0
j = 0

while lon<=elon:
	lat = slat
	while lat<=elat:
		workeff = cal_work_eff(lon,lat,pdata)
		lateff = cal_lat_eff(lat,pdata)
		cur = {
			'lat':lat,
			'lon':lon,
			'workeff':workeff,
			'lateff':lateff
			}
		pp.pprint(cur)
		result.append(cur)
		lat += 5
	lon += 10




