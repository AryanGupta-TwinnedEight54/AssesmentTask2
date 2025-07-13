from datetime import timedelta
import random
class Tram: # Done by Aryan
    def __init__(self, id, capacity, current_passenger=0, current_location = 'NL',):
        self.id = id
        self.current_passengers = current_passenger
        self.location = current_location
        self.capacity = capacity
    def board(self, passengers):
        if self.current_passengers + passengers > self.capacity:
            print('TRAM FULL')
        if self.current_passengers + passengers <= self.capacity:
            self.current_passengers += passengers

        
    def depart(self, passengers):
        if self.current_passengers - passengers < self.capacity:
           print('THERE IS LESS PASSENGER THAN ON THE TRAM')
        if self.current_passengers - passengers >- self.capacity:
            self.current_passengers -= passengers
    def move_to(self, location):
        self.location = location
 
    
# Class containing information about each tram station.
class Station: # Done by Caden
    def __init__(self, station_name, waiting_passengers=30):
        # waiting_passengers is the number of passengers waiting at a station.
        self.waiting_passengers = waiting_passengers
        # station_name is the name of the station that a tram is arriving at.
        station_name = "Carlingford"
        self.station_name = station_name
    # Prints an output stating the number of passengers waiting at a certain station.
    def total(self, station_name, waiting_passengers):
        print(self.station_name + " station has at total of " + self.waiting_passengers + " passengers waiting.")

        
        
tram_passenger_limit = 0
peak_hours = [[timedelta(6,30), timedelta(8,30)],[timedelta(15,00), timedelta(18,00)]]
offpeak_interval = timedelta(15)
peak_interval = timedelta(7, 30)
num_trams = 16
tram_station_name_list = ["Westmead","Westmead Hospital","Children’s Hospital","Ngara (T-ways)", "Fennell Street","Prince Alfred Square", "Parramatta Square", "Parramatta","Robin Thomas", "Camellia","Rydalmere", "Dundas","Telopea", "Carlingford"]
station_list = []
tram_list = []

for name in tram_station_name_list:
    station = Station(station_name=name, waiting_passengers=random.randint(20,30))
    station_list.append(station)


for i in range(num_trams):
    tram = Tram(id=i, capacity=None)
    tram_list.append(tram)