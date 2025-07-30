# Created by Caden
# Imports 'timedelta' class from 'datetime' library.
from datetime import timedelta

# Creates 'Station' class, containing information about every tram station in the system.
class Station:
    def __init__(self, name):
        self.name = name

# Creates 'Tram' class, containing information about every tram within the system.
class Tram:
    def __init__(self, tram_id, direction):
        self.tram_id = tram_id
        self.status = "available"
        self.current_trip = None
        self.direction = direction
        self.capacity = 0

    # Function that sets a tram into the system.
    def assign_to_trip(self, trip):
        # Checks if a tram is not currently in the system and then puts a tram into it.
        if self.status == "available":
            self.status = "in_use"
            self.current_trip = trip 
            # Creates 'output' variable to print timetable rows for each tram's time.
            output = f"Tram {self.tram_id}  -"
            output_capacity = ""
            # Sets 'j' to increments of 3 between 0 and 48.
            for j in range(0,48,3):
                    # Constantly increases a tram's time output by 3 minutes, stopping at each station, until 48 minutes has passed.
                    output += f"   {self.current_trip.start_time+timedelta(minutes=(int(j)))}"
                    # Checks to see if the current time is within the peak hours.
                    if current_time >= morning_peak_start and current_time < morning_peak_end or current_time >= afternoon_peak_start and current_time < afternoon_peak_end:
                        self.capacity += 31
                    else:
                        self.capacity += 18
                    # Ensures tram capacity does not exceed the maximum of 400 passengers.
                    if self.capacity >= max_capacity:
                        self.capacity = max_capacity
                    output_capacity += f"       {self.capacity}"
            # Sets variable 'direction_index' for which timetable a tram's data is to be put in (forward or backward), depending on which direction a tram is heading.
            if self.direction == 'F':
                direction_index = 0
            else:
                direction_index = 1
            # Fills 'output_array' with the numeric value for a tram's direction and also adds the incrementing time and capacity values alongside it.
            output_array[direction_index].append(output + "\nCapacity: " + output_capacity)

    # Function that pulls a tram out of the system.
    def release_from_trip(self):
        self.status = "available"
        self.current_trip = None
        self.capacity = 0
        # Swaps a tram's direction, as it has reached the end of the line.
        if self.direction == "F":
            self.direction = "B"
        else:
            self.direction = "F"

   
# Creates 'Trip' class, containing information about whenever a tram is currently running in the system or not.
class Trip:
    def __init__(self, start_time):
        self.start_time = start_time
        self.end_time = ""

# Creates 'Tram_Controller' class, containing information about when to push a tram into the system or to pull a tram out of it.
class Tram_Controller:
    def __init__(self, trams_list):
        self.trams = trams_list

    # Function that allows for an available tram to be grabbed and put into the system.
    def get_available_tram(self,direction):
        for tram in self.trams:
            # Checks if a tram is available and is heading in the same direction that it needs to be sent in.
            if tram.status == "available" and tram.direction == direction:
                return tram
        return None
    
    # Function that checks when to pull a tram out of the system, specifically once it has made a full trip from Carlingford to Westmead.
    def release_completed_trams(self, current_time):
        for tram in self.trams:
            if tram.status == "in_use":
                if tram.current_trip.start_time+timedelta(minutes=48) <= current_time:
                    tram.release_from_trip()

    # Function used for passengers to board the tram when it has reached a station.
    def passenger_boarding(self, current_time):
       # Checks if a tram is currently in the system and has stopped at a station.
       for tram in self.trams:
            if tram.status == "in_use":
                for j in range(0,48,3):
                    if tram.current_trip.start_time+timedelta(minutes=(int(j))) == current_time:
                        # Checks whether the time is within peak hours or outside peak hours.
                        if current_time >= morning_peak_start and current_time < morning_peak_end or current_time >= afternoon_peak_start and current_time < afternoon_peak_end:
                            # Increases total number of passengers on board a tram by 31, if the time is within peak hours.
                            tram.capacity += 31
                        else:
                            # Increases total number of passengers on board a tram by 18, if the time is outside peak hours.
                            tram.capacity += 18
                        # Ensures total passengers on board tram do not exceed the tram's maximum capacity.
                        if tram.capacity >= max_capacity:
                            tram.capacity = max_capacity

# Creates 'Timetable' class, containing information on creating a timetable using the trips of each tram throughout the system.
class Timetable:
    def __init__(self, list_of_trips):
        self.trips = list_of_trips

# Setting multiple variables and arrays.
output_array = [[],[]]
start_time = timedelta(hours = 6, minutes = 30)
end_time = timedelta(hours = 19)
current_time = start_time
#tram_station_name_list = ['Carlingford', 'Telopea', 'Dundas', 'Yallamundi', 'Rosehill Gardens', 'Tramway Avenue', 'Robin Thomas', 'Parramatta Square', 'Church Street', 'Prince Alfred Square', 'Fennell Street', 'Benaud Oval', 'Ngara', 'Childrens Hospital', 'Westmead Hospital', 'Westmead']
tram_station_name_list = ['Carling', 'Telopea', 'Dundas ', 'Yllmndi', 'R Grdns', 'Tram Av', 'Robin T', 'Parr Sq', 'Chur St', 'P Al Sq', 'Fenn St', 'Bena Ov', 'Ngara  ', 'Child H', 'Westm H', 'Wstmead']
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


# Ties every station to the station class and adds it to a list.
for name in tram_station_name_list:
    station = Station(name=name)
    stations.append(station)

# Creates a list of every trip that a tram will take based on its start time.
while current_time <= end_time:
    # Defines a trip under the variable 'trip_single'.
    trip_single = Trip(start_time=current_time)
    # Adds every trip to an array called 'trips'.
    trips.append(trip_single)
    # Changes the time interval of trams whether it is peak hour or not.
    if current_time >= morning_peak_start and current_time < morning_peak_end or current_time >= afternoon_peak_start and current_time < afternoon_peak_end:
        current_time += duration/2
    else:
        current_time += duration

# Sets timetable containing all trips to a variable.
timetable = Timetable(list_of_trips=trips)
active_trips = []

# Sets current time to the beginning time of the program.
current_time = start_time
# Creates a variable called 'all_trams', set to a list containing all 16 trams for the program, creating them as objects and defining their tram id and direction.
all_trams = [Tram(1,"F"), Tram(2,"B"), Tram(3,"F"), Tram(4,"B"), Tram(5,"F"), Tram(6,"B"), Tram(7,"F"), Tram(8,"B"), Tram(9,"F"), Tram(10,"B"), Tram(11,"F"), Tram(12,"B"), Tram(13,"F"), Tram(14,"B"), Tram(15,"F"), Tram(16,"B")]

# Puts list containing all trams into Tram_Controller class and sets it to a variable.
tram_controller = Tram_Controller(all_trams)

# Runs while the program is within the designated timeframe.
while current_time < end_time:
    # Runs for every trip that each tram has.
    for trip in timetable.trips:
        if trip.start_time == current_time:
            # Defines available forward trip trams (Carlingford-Westmead)
            available_tram = tram_controller.get_available_tram("F")
            if available_tram:
                available_tram.assign_to_trip(trip)

            # Defines available backward trip trams (Westmead-Carlingford)
            available_tram = tram_controller.get_available_tram("B")
            if available_tram:
                available_tram.assign_to_trip(trip)

    # Runs passenger boarding process.
    tram_controller.passenger_boarding(current_time)

    # Runs process which pulls a tram that reached the end of the line out of the system.
    tram_controller.release_completed_trams(current_time)
    
    # Constantly increments the time by 30 seconds.
    current_time += timedelta(seconds = 30)

# Prints forward timetable
location_output = "            "
# For every station name in the station name list, insert and format it into an empty variable 'location_output'.
for name in tram_station_name_list:
    # Adds every station name to 'location_output' and restricts every name to the first 7 characters for formatting.
    location_output += name[:7] + "   "

# Prints out names of stations at the top of the timetable.
print (location_output)

# Prints every set of times for every tram travelling forward (Carlingford - Westmead).
for rowtime in output_array[0]:
    print(rowtime)

# Gap in between timetables for formatting.
print("")

# Prints backward timetable
# Sets 'location_output' back to an empty variable.
location_output = "            "
# For every station name in the station name list, insert and format it into an empty variable 'location_output'.
for name in reversed(tram_station_name_list):
    # Adds every station name to 'location_output' and restricts every name to the first 7 characters for formatting.
    location_output += name[:7] + "   "

# Prints out names of stations at the top of the timetable.
print (location_output)

# Prints every set of times for every tram travelling forward (Westmead - Carlingford).
for rowtime in output_array[1]:
    print(rowtime)

