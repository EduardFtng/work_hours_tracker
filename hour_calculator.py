import json
from datetime import date, datetime, time


# function to print all the data stored in .json
def print_data(filename='info.json'):
    with open('info.json') as json_file:
        data = json.load(json_file)

    print(data)

# function to add the data to JSON-file
def write_data(data, filename='info.json'):
    with open('info.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# function to calculate the sum of all hours
def sum_of_all_hours(filename='info.json'):
    with open('info.json') as json_file:
        data = json.load(json_file)

    time_format = '%H:%M:%S'
    hours_sum = 0

    for i in data['Info']:

        # Get the Values from each(start and end) dict entry
        start = datetime.strptime(i['start'], time_format)
        end = datetime.strptime(i['end'], time_format)
        pause_h = i['pause']

        diff = end - start

        # Convert the diff into seconds and devide with 3.600 to get hours
        hours = (diff.seconds) / 3600
        
        # Add up the hours to the sum
        hours_sum += hours - pause_h
        
    return hours_sum


def calculate_pause_in_h(pause_min):
    pause_h = pause_min / 60
    return pause_h


def calculate_hours_till_8_pm(start_time_hour, start_time_minute, end_time_hour, end_time_minute):

    time_format = '%H:%M:%S'
    
    # Casting time into string and the string into datetime to be able to use the minus opperation 
    start = datetime.strptime(str(time(start_time_hour, start_time_minute)), time_format)
    end = datetime.strptime(str(time(end_time_hour, end_time_minute)), time_format)
    
    if end < datetime.strptime(str(time(20, 0)), time_format):

        diff = end - start
        
        x = (diff.seconds) / 3600

        hours_till_8_pm = x
    
    else:

        diff = datetime.strptime(str(time(20, 0)), time_format) - start

        x = (diff.seconds) / 3600

        hours_till_8_pm = x
        
    return hours_till_8_pm


def calculate_hours_50_perc(end_time_hour, end_time_minute):
    
    time_format = '%H:%M:%S'
    
    # Casting time into string and the string into datetime to be able to use the minus opperation 
    start = datetime.strptime(str(time(20, 0)), time_format)
    end = datetime.strptime(str(time(end_time_hour, end_time_minute)), time_format)
    
    # If the ending time of the shift is earlier then 8pm, set hours_50_perc to 0.
    if start < end:
        # Calculating the hours after 8pm
        diff = end - start

        # Converting the diff into seconds
        x = (diff.seconds) / 3600

        hours_50_percs = x
    else:
        hours_50_percs = 0
    

    return hours_50_percs


# write_data(data)
# print_data()

while True:
    # Load the .json file into the data variable
    with open('info.json') as json_file:
        data = json.load(json_file)

        # temp variable to save dict into data with new added values
        temp = data['Info']

    print()
    print('Set the date.')
    year = int(input('Year: '))
    month = int(input('Month: '))
    day = int(input('Day: '))

    print('Was it a Sunday or an holiday?')
    b_sunday = input('Yes → y or No → n: ')
    if b_sunday == 'y':
        b_sunday = True
    if b_sunday == 'n':
        b_sunday = False
    
    print('When did the shift start?')
    start_time_hour = int(input('Hour: '))
    start_time_minute = int(input('Minute: '))

    print('When did the shift end? (Hour, Minute):')
    end_time_hour = int(input('Hour: '))
    end_time_minute = int(input('Minute: '))

    print('How long was your break?')
    pause_min = int(input('Minutes: '))

    
    pause_h = calculate_pause_in_h(pause_min)

    hours_till_8_pm = calculate_hours_till_8_pm(start_time_hour, start_time_minute, end_time_hour, end_time_minute) - pause_h

    # Getting a value for plus 50% hours
    p_50_perc = calculate_hours_50_perc(end_time_hour, end_time_minute)
    
    

    y = {
        "date": str(date(year, month, day)),
        "sunday_holiday": b_sunday,
        "start": str(time(start_time_hour, start_time_minute)),
        "end": str(time(end_time_hour, end_time_minute)),
        "pause": pause_h,
        "hours_till_8_pm": hours_till_8_pm,
        "plus_50_perc": p_50_perc
    }
    
    # Appending new data(y) to temp details
    temp.append(y)

    print('Are the give informations correct?')
    print(y)

    print('Do you want to save the data?')
    valdiation = input('Yes → y or No → n: ')
    if valdiation == 'y':
        write_data(data)
        print('Successfully saved.')
        print('Current sum of hours: ' + str(sum_of_all_hours()))
        print()
        break
    else:
        print('Process terminated.')
        break

