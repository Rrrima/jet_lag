from utils import *
from data import *
from city import Grid
import pprint
pp = pprint.PrettyPrinter(indent=4)
# main
def start_iteration(lonst,latst,lon1,lon2,lat1,lat2):
	lon = lon1
	lonl = int((lon2-lon1)/lonst)+1
	r = init_arr(lonl)
	i = 0

	while lon<=lon2:
		lat = lat1
		while lat<=lat2:
			workeff = cal_work_eff(lon,lat,pdata)['result']
			lateff = cal_lat_eff(lat,pdata)['result']
			r[i].append(Grid(lat,lon,workeff,lateff))
			lat += latst
		lon += lonst
		i += 1
	return r

def regularize_gird(grids):
	total_workeff = []	
	total_lateff = []
	for eachline in grids:
		for each in eachline:
			total_workeff.append(each.workeff)
			total_lateff.append(each.lateff)
	minw = min(total_workeff)
	maxw = max(total_workeff)
	minl = min(total_lateff)
	maxl = max(total_lateff)
	#print(minw,maxw,minl,maxl)
	for eachline in grids:
		for each in eachline:
			each.reset_workeff((each.workeff-minw)/(maxw-minw))
			each.reset_lateff((each.lateff-minl)/(maxl-minl))



pdata = participants_data() # (lat,lon)
range_of_lon = get_lon_range(pdata)
range_of_lat = get_lat_range(pdata)

slon = range_of_lon[0]+30
slat = range_of_lat[0]
elon = range_of_lon[1]+30
elat = range_of_lat[1]
print(slon,elon,slat,elat)

result = start_iteration(10,3,slon,elon,slat,elat)
regularize_gird(result)
arr = generate_attr(result,'score')
print(arr)
draw_heatmap(arr)

#  print out attributes
for eachline in result:
	for each in eachline:
		each.printout()






