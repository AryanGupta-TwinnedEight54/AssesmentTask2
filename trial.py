from datetime import timedelta
import random
class Tram:
    def __init__(self, tram_id, capacity, current_location, direction, current_passenger=0, stations_traversed=0):
        self.id = tram_id
        self.current_passengers = current_passenger
        self.location = current_location
        self.capacity = capacity
        self.direction = direction
        self.stations_traversed = stations_traversed
    def board(self, passengers):
        if self.current_passengers + passengers > self.capacity:
            print('TRAM FULL')
        if self.current_passengers + passengers <= self.capacity:
            self.current_passengers += passengers

        

        
tram_passenger_limit = 0
peak_hours = [
    [timedelta(hours=6, minutes=30), timedelta(hours=8, minutes=30)],
    [timedelta(hours=15), timedelta(hours=18)]
]

offpeak_interval = timedelta(minutes=15)
peak_interval = timedelta(minutes=7, seconds=30)
num_trams = 16
tram_station_name_list = ["Westmead", "Westmead Hospital", "Childrens Hospital","Ngara", "Benaud Oval", "Fennell Street", "Prince Alfred Square", "Church Street", "Parramatta Square", "Robin Thomas", "Tramway Avenue"," Rosehill Gardens", "Yallamundi", "Dundas", "Telopea","Carlingford"]
station_list = []
tram_list = []
start_time = timedelta(hours=6, minutes=30)
current_time = start_time
end_time = timedelta(hours=20, minutes=30)

tram_list = []
