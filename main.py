from datetime import time

class Tram: # Done by Aryan
    def __init__(self, id, current_location,capacity, current_passenger=0):
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
 
    
# (need to add station name and change add and remove passengers to 'waiting passengers'.)
class Station: # Done by Caden
    def __init__(self, station_name, waiting_passengers):
        # waiting_passengers is the number of passengers waiting at a station.
        waiting_passengers = 30
        self.waiting_passengers = waiting_passengers
        # station_name is the name of the station that a tram is arriving at.
        station_name = "Carlingford"
        self.station_name = station_name
    # Prints an output stating the number of passengers waiting at a certain station.
    def total(self, station_name, waiting_passengers):
        print(self.station_name + " station has at total of " + self.waiting_passengers + " passengers waiting.")

        
        
calingord = Station(50, 30)
calingord.total(2)


peak_hours = [[time(6,30), time(8,30)],[time(15,00), time(18,00)]]
