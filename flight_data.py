# get flight data from Flightradar24
from pyflightdata import FlightData 
f = FlightData()
#f.login('rimacyn@gmail.com','lansezuoERER1997')
# get the last 5 flights for AI101
lf = f.get_history_by_flight_number('AI101')[-5:]
#for each in lf:
	#print(each)

# get all the airlines
all_air_ports = f.get_airports('China')
#print(all_air_ports)

flight_dict = f.get_flights_from_to('JDZ','KCA')
for each in flight_dict:
	print(each)