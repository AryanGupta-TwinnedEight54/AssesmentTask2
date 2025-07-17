from datetime import timedelta

start_time = timedelta(hours=6, minutes=30)
end_time = timedelta(hours= 7)
current_time = start_time

while current_time < end_time:
    x = timedelta(minutes=25)
    current_time += x
    print(current_time)