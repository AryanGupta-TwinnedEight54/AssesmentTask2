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
            self.current_passengers = self.capacity
        if self.current_passengers + passengers <= self.capacity:
            self.current_passengers += passengers

        
    def depart(self):
        departing = random.randint(0, self.current_passengers)
        self.current_passengers -= departing
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
        if  '.5' in str(self.location):
            return False
        else:
            return True
    def change_direction(self):
        if self.direction == 0 or self.direction == 0.0:
            self.direction = 1
            self.location = 0.5
        elif self.direction == 1 or self.direction == 1.0:
            self.direction = 0
            self.location = 0.5


# (need to add station name and change add and remove passengers to 'waiting passengers'.)
class Station: # Done by Caden
    def __init__(self, station_name, waiting_passengers=80):
        # waiting_passengers is the number of passengers waiting at a station.
        self.waiting_passengers = waiting_passengers
        # station_name is the name of the station that a tram is arriving at.
        station_name = station_name
        self.station_name = station_name
    # Prints an output stating the number of passengers waiting at a certain station.
    
    def board(self, tram):
        if self.station_name in ['Robin Thomas',  'Parramatta Square', 'Church Street', 'Prince Alfred Square']:
            tram.current_passengers = tram.capacity 
        elif tram.capacity == 400:
            self.waiting_passengers = random.randint(400, 600)
            amount_boarded = random.randint(200, 400)
            tram.board(amount_boarded)
            self.waiting_passengers -= amount_boarded
        else:
            self.waiting_passengers = random.randint(200, 250)
            amount_boarded = random.randint(0,200)
            tram.board(amount_boarded)
            self.waiting_passengers -= amount_boarded

        
        
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
user_start = input('Please enter user start time(to generate full timetable press enter) in DD:HH:MM ')
if user_start == '':
    start_time = timedelta(hours=5, minutes=00)
    current_time = start_time
    end_time = timedelta(days = 1, hours=1, minutes=00)
else:
    split_time = user_start.split(':')
    start_time = timedelta(days=int(split_time[0]), hours=int(split_time[1]), minutes=int(split_time[2]))
    current_time = start_time
    user_end = input('Please enter user end time')
    user_end_split = user_end.split(':')
    end_time = timedelta(days=int(user_end_split[0]), hours=int(user_end_split[1]), minutes=int(user_end_split[2]))

for name in tram_station_name_list:
    station = Station(station_name=name, waiting_passengers=random.randint(20,30))
    station_list.append(station)

tram_list = []
loc = 1
even = 0
id = 0

for i in range(int(num_trams / 2)):
    loc -= 1
    even += 1
    if even % 2 == 0:
        tram = Tram(tram_id=id, direction=1, current_location=loc, tram_peak=False, capacity=80)
        id += 1
        tram1 = Tram(tram_id=id, direction=0, current_location=loc, tram_peak=False, capacity=80)
        id += 1
    else:
        tram = Tram(tram_id=id, direction=1, current_location=loc, tram_peak=True, capacity=80)
        id += 1
        tram1 = Tram(tram_id=id, direction=0, current_location=loc, tram_peak=True, capacity=80)
        id += 1

    tram_list.append(tram)
    tram_list.append(tram1)


# Done by Caden

def ispeak():
    if any(start <= current_time <= end for start, end in peak_hours):
        return True
    else:
        return False

def peak_timing():
    # Get total hours and minutes from the timedelta
    total_seconds = current_time.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)

    # Convert to total minutes for easy comparison
    current_minutes = hours * 60 + minutes

    # 7:00 AM = 420 minutes, 7:00 PM = 1140 minutes
    return 420 <= current_minutes <= 1140

# Done by Aryan, Note Caden did annother function before me but I accedintantly deleted that commit while trying to delete my commit


def format_time(t: timedelta, use_12hr=False):
    total_seconds = int(t.total_seconds())
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    if use_12hr:
        suffix = 'AM'
        if hours >= 12:
            suffix = 'PM'
            if hours > 12:
                hours -= 12
        elif hours == 0:
            hours = 12
        time_str = f'{hours:02}:{minutes:02}:{seconds:02} {suffix}'
    else:
        time_str = f'{hours:02}:{minutes:02}:{seconds:02}'

    if days > 0:
        return f'{days}d {time_str}'
    else:
        return time_str


setting_preferance = input('Do you want it in 24 hour yes or no: ')
use_24_hour_time = None
if setting_preferance == 'no':
    print('Works')
    use_24_hour_time = False
else:
    use_24_hour_time = True


while current_time <= end_time:
    for tram in tram_list:
        if ispeak():
            tram.capacity = 400
        else:
            tram.capaicity = 200
        
        if tram.location < 0:
            tram.move_to(1)
        elif tram.location >= 0:
            if tram.direction == 1 and tram.on_station() and tram.on_track:
                tram.depart()
                
                station = station_list[int(tram.location)]
                print(f'tram {tram.id} is at station {station.station_name} with {tram.current_passengers} passengers')
                station.board(tram)
               

            if tram.direction == 0 and tram.on_station() and tram.on_track:
                opposite_station_list = station_list[::-1]
                station = opposite_station_list[int(tram.location)]
                tram.depart()
                
                print(f'tram {tram.id} is at station {opposite_station_list[int(tram.location)].station_name} with {tram.current_passengers}')
                station.board(tram)
        
            tram.move_to(0.5)
            
        if tram.location == 16.0:
            tram.change_direction()
        if peak_timing() and tram.on_track == False:
            tram.deploy()
        if peak_timing() == False and tram.tram_peak:
            tram.on_track = False

        

            
        

            
    current_time += timedelta(minutes=7, seconds=30)
    if use_24_hour_time:
        print("Current time:", format_time(current_time, use_12hr=False))
    if use_24_hour_time == False:
        print("Current time:", format_time(current_time, use_12hr=True))