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
    def __init__(self, add_passengers, remove_passengers):
        # add_passengers is the number of passengers waiting at a station.
        add_passenger = 30
        self.add_passengers = add_passengers
        # remove_passengers is the number of passengers waiting at a station that are now boarding a tram.
        remove_passenger = 15
        self.remove_passengers = remove_passengers

    def total(self, add_passengers):
        print("This station has" + self.add_passengers + "passengers.")

    def leaving_passengers(self, remove_passengers):
        print(remove_passengers + "passengers have left the station.")
        
        
calingord = Station(50, 30)
calingord.total(2)