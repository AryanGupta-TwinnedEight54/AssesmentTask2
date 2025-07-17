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


for i in range(num_trams):
    tram = Tram(id=i, capacity=None)
    tram_list.append(tram)

# Done by Caden

def is_peak(current_time):
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
    

while current_time < end_time:
    if is_peak(current_time):
        time_interval = peak_interval
    else: 
        time_interval = offpeak_interval
    current_time = current_time +time_interval
    print("Current time:", format_time(current_time))
