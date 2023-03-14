def get_days_later(days):
    if days == 1:
        return "(next day)"
    elif days > 1:
        return "(%s days later)" %(days)
    return " "

def add_time(start_time, duration, day = False):
    # Days of the week
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    #Seperate everything before the colon
    start_time_a = start_time.split(':')[0] # 2
    duration_a = duration.split(':')[0] # 305

    #Seperate everything after the colon
    start_time_NO_AM_PM = start_time.split()[0] # 2:15
    start_time_b = start_time_NO_AM_PM.split(':')[1] #15
    duration_b = duration.split(':')[1] # 10

    #Find the AM or PM
    am_or_pm = start_time.split()[1] #PM

    #Calculate the time
    total_hours = int(start_time_a) + int(duration_a)
    total_minutes = int(start_time_b) + int(duration_b)

    if total_minutes >= 60:
        total_hours += int(total_minutes) / 60
        total_minutes = int(total_minutes) % 60

    days_later = 0
    if am_or_pm == 'PM' and total_hours > 12:
        if total_hours % 24 >= 1.0:
            days_later += 1

    if total_hours >= 12:
        hours_left = total_hours / 24
        days_later += int(hours_left)

    total_hr = total_hours
    while True:
        if total_hr < 12:
            break
        if total_hr >= 12:
            if am_or_pm == "AM":
                am_or_pm = "PM"
            elif am_or_pm == "PM":
                am_or_pm = "AM"
            total_hr -= 12

    final_hr = int(total_hours) % 12 or int(start_time_a) + 1
    final_min = int(total_minutes) % 60

    time = str(final_hr) + ':' + str(final_min).zfill(2) + ' ' + str(am_or_pm) 

    # Find Day of the Week
    if day:
        day = day.lower()
        future_day = int(days_of_week.index(day) + days_later) % 7
        current_day = days_of_week[future_day]
        time += f', {current_day.title()} {get_days_later(days_later)}'
    else:
        time = time + " " + get_days_later(days_later)
        

    return time.strip()

print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)