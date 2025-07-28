from datetime import timedelta

current_time = timedelta(hours=6, minutes=30)
peak_hours = [
    [timedelta(hours=6, minutes=30), timedelta(hours=8, minutes=30)],
    [timedelta(hours=15), timedelta(hours=18)]
]

def ispeak():
    if any(start <= current_time <= end for start, end in peak_hours):
        return False
    else:
        return True

print(ispeak())