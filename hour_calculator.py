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
def calculate_hours(filename='info.json'):
    with open('info.json') as json_file:
        data = json.load(json_file)

    time_format = '%H:%M:%S'
    hours_sum = 0

    for i in data['Info']:

        # Get the Values from each(start and end) dict entry
        start = datetime.strptime(i['start'], time_format)
        end = datetime.strptime(i['end'], time_format)
        diff = end - start

        # Convert the diff into seconds and devide with 3.600 to get hours
        hours = (diff.seconds) / 3600
        
        # Add up the hours to the sum
        hours_sum += hours
        
        return hours_sum

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

    print('Was it a Sunday?')
    b_sunday = input('Yes → y or No → n: ')
    if b_sunday == "y":
        b_sunday = True
    if b_sunday == "n":
        b_sunday = False
    
    print('When did the shift start?')
    start_time_hour = int(input('Hour: '))
    start_time_minute = int(input('Minute: '))

    print('When did the shift end? (Hour, Minute):')
    end_time_hour = int(input('Hour: '))
    end_time_minute = int(input('Minute: '))

    y = {
        "date": str(date(year, month, day)),
        "sunday": b_sunday,
        "start": str(time(start_time_hour, start_time_minute)),
        "end": str(time(end_time_hour, end_time_minute))
    }
    
    # appending data to temp details
    temp.append(y)

    print('Are the give informations correct?')
    print(y)

    print('Do you want to save the data?')
    valdiation = input('Yes → y or No → n: ')
    if valdiation == "y":
        write_data(data)
        print('Successfully saved.')
        print('Current sum of hours: ' + str(calculate_hours()))
        print()
        break
    else:
        print('Process terminated.')
        break

