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

        
    def depart(self, passengers):
        if self.current_passengers - passengers < self.capacity:
           print('THERE IS LESS PASSENGER THAN ON THE TRAM')
        if self.current_passengers - passengers >- self.capacity:
            self.current_passengers -= passengers
    def move_to(self, location):
        self.location += location
 
    
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
tram_station_name_list = ["Westmead","Westmead Hospital","Children’s Hospital","Ngara (T-ways)", "Fennell Street","Prince Alfred Square", "Parramatta Square", "Parramatta","Robin Thomas", "Camellia","Rydalmere", "Dundas","Telopea", "Carlingford"]
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
for i in range(num_trams):
    loc -= 1
    direction = 1 if i % 2 == 0 else 0
    tram = Tram(tram_id=i, direction=direction, current_location=loc, capacity=12312)
    tram_list.append(tram)


# Done by Caden

def time_interval_finder(current_time):
    if any(start <= current_time <= end for start, end in peak_hours):
        return peak_interval
    else:
        return offpeak_interval

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
    for tram in tram_list:
        if tram.location < 0:
            tram.move_to(1)
        elif tram.location >= 0:
            if tram.direction == 1:
                print(f'{tram_station_name_list[tram.location]} tram id is {tram.id}')
            if tram.direction == 0:
                x = tram_station_name_list[::-1]
                print(f'{x[tram.location]} tram id is {tram.id}')
                
            tram.move_to(1)
            
        if tram.location == 14:
            if tram.direction == 0:
                tram.direction = 1
                tram.location = 0
            else:
                tram.direction = 0
                tram.location = 0

     
    current_time += time_interval_finder(current_time)
    print("Current time:", format_time(current_time, use_12hr=True))