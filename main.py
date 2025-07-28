from datetime import timedelta
import random
class Tram:
    def __init__(self, tram_id, capacity, current_location, direction,  tram_peak, current_passenger=0, stations_traversed=0):
        self.id = tram_id
        self.current_passengers = current_passenger
        self.location = current_location
        self.capacity = capacity
        self.direction = direction
        self.stations_traversed = stations_traversed
        self.tram_peak = tram_peak
        self.on_track = None
        if self.tram_peak == True:
            self.on_track = False
        else:
            self.on_track = True
                    
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
    def move_to(self, movement):
        if movement == 1:
            self.location += 1
        else:
            self.location += 0.5
    def deploy(self):
        self.on_track = True
    def remove(self):
        self.on_track = False
    def should_be_on_track(self):
        return self.on_track
    def on_station(self):
        if  '0.5' in str(self.location):
            return False
        else:
            return True
    



 
    
# (need to add station name and change add and remove passengers to 'waiting passengers'.)
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

for name in tram_station_name_list:
    station = Station(station_name=name, waiting_passengers=random.randint(20,30))
    station_list.append(station)

tram_list = []
loc = 1
even = 0
id = 0
for i in range(int(num_trams/2)):

    loc -= 1
    if i % 2 == 0:
        tram = Tram(tram_id=id, direction=1, current_location=loc, tram_peak=False, capacity=None)
        id +=1
        tram1 = Tram(tram_id=id, direction=0, current_location=loc, tram_peak=False, capacity=None)
        id +=1
    else:
        tram = Tram(tram_id=id, direction=1, current_location=loc, tram_peak=True, capacity= None)
        id +=1
        tram1 = Tram(tram_id=id, direction=0, current_location=loc, tram_peak=True, capacity=None)
        id +=1
    tram_list.append(tram)
    tram_list.append(tram1)
# Done by Caden

def ispeak():
    if any(start <= current_time <= end for start, end in peak_hours):
        return True
    else:
        return False

# Done by Aryan, Note Caden did annother function before me but I accedintantly deleted that commit while trying to delete my commit
def format_time(t, use_12hr=False):
    t = str(t)
    t = t.split(':')
    hours = int(t[0])
    minutes = t[1]
    seconds = t[2]
    if use_12hr:
        suffix = ''
        if hours > 12:
            suffix = 'PM'
            hours = hours - 12
        else:
            suffix = 'AM'
        return f'{hours}:{minutes}:{seconds}:{suffix}'
    elif use_12hr == False:
        return f'{hours}:{minutes}:{seconds}'
        
    
for i in range(10):
    for tram in trams:
        if tram.location < 0:
            tram.move_to(1)
        elif tram.location >= 0:
            if tram.direction == 1 and tram.on_station() and tram.should_be_on_track():
                print(f'tram {tram.id} is at station {tram_station_name_list[int(tram.location)]}')
            if tram.direction == 0 and tram.on_station() and tram.should_be_on_track():
                x = tram_station_name_list[::-1]
                print(f'tram {tram.id} is at station {x[int(tram.location)]}')
        
        tram.move_to(0)
            
        if tram.location == 14:
            if tram.direction == 0:
                tram.direction = 1
                tram.location = 0
            else:
                tram.direction = 0
                tram.location = 0 
        

            
    current_time += timedelta(minutes=7, seconds=30)
    print("Current time:", format_time(current_time, use_12hr=True))