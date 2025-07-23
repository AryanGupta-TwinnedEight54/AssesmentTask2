from datetime import timedelta

class Station:
    def __init__(self, name):
        self.name = name

class Tram:
    def __init__(self, tram_id, direction):
        self.tram_id = tram_id
        self.status = "available"
        self.current_trip = None
        self.direction = direction

    def assign_to_trip(self, trip):
        if self.status == "available":
            self.status = "in_use"
            self.current_trip = trip
            print("Tram: ", self.tram_id," Status: ", self.status)

    def release_from_trip(self):
        self.status = "available"
        self.current_trip = None
        if self.direction == "F":
            self.direction = "B"
        else:
            self.direction = "F"

class Trip:
    def __init__(self, start_time):
        self.start_time = start_time
        self.end_time = ""

class Tram_Controller:
    def __init__(self, trams_list):
        self.trams = trams_list

    def get_available_tram(self,direction):
        for tram in self.trams:
            if tram.status == "available" and tram.direction == direction:
                return tram
        return None
    
    def release_completed_trams(self, current_time):
        for tram in self.trams:
            if tram.status == "in_use":
                if tram.current_trip.start_time+timedelta(minutes=48) <= current_time:
                    tram.release_from_trip()

class Timetable:
    def __init__(self, list_of_trips):
        self.trips = list_of_trips


start_time = timedelta(hours = 6, minutes = 30)
end_time = timedelta(hours = 19)
current_time = start_time
tram_station_name_list = ['Carlingford', 'Telopea', 'Dundas', 'Yallamundi', 'Rosehill Gardens', 'Tramway Avenue', 'Robin Thomas', 'Parramatta Square', 'Church Street', 'Prince Alfred Square', 'Fennell Street', 'Benaud Oval', 'Ngara', 'Childrens Hospital', 'Westmead Hospital', 'Westmead']
stations = []
trams = []
trips = []
duration = timedelta(minutes = 15)
x = 0
direction_flag = "F"
capacity = 0
morning_peak_start = timedelta(hours = 7)
morning_peak_end = timedelta(hours = 8, minutes = 30)
afternoon_peak_start = timedelta(hours = 15)
afternoon_peak_end = timedelta(hours = 18)
max_capacity = 400

#Populate Stations
for name in tram_station_name_list:
    station = Station(name=name)
    stations.append(station)

#Populate Trams - now done with array below
#for i in range(0,16):
#    tram = Tram(tram_id=i)
#    trams.append(tram)

while current_time <= end_time:

    
    #print (current_time, " -- Tram Starting: ", x+1)
    trip_single = Trip(start_time=current_time)
    trips.append(trip_single)
    if current_time >= morning_peak_start and current_time < morning_peak_end or current_time >= afternoon_peak_start and current_time < afternoon_peak_end:
        current_time += duration/2
        #capacity += 31
    else:
        current_time += duration
        #capacity += 18

   # if capacity >= max_capacity:
    #    capacity = max_capacity



timetable = Timetable(list_of_trips=trips)
#print(dir(timetable))
active_trips = []

current_time = start_time
all_trams = [Tram(1,"F"), Tram(2,"B"), Tram(3,"F"), Tram(4,"B"), Tram(5,"F"), Tram(6,"B"), Tram(7,"F"), Tram(8,"B"), Tram(9,"F"), Tram(10,"B"), Tram(11,"F"), Tram(12,"B"), Tram(13,"F"), Tram(14,"B"), Tram(15,"F"), Tram(16,"B")]

tram_controller = Tram_Controller(all_trams)

while current_time < end_time:

    for trip in timetable.trips:
        if trip.start_time == current_time:
            #Forward Trip Trams (Carlingford-Westmead)
            print(current_time, "Carlingford-Westmead")
            available_tram = tram_controller.get_available_tram("F")
            if available_tram:
                available_tram.assign_to_trip(trip)
            #active_trips.append(trip)

            #Return Trip Trams (Westmead-Carlingford)
            print(current_time, "Westmead-Carlingford")
            available_tram = tram_controller.get_available_tram("B")
            #print(available_tram)
            if available_tram:
                available_tram.assign_to_trip(trip)
            #active_trips.append(trip)
    tram_controller.release_completed_trams(current_time)
    current_time += timedelta(seconds = 30)