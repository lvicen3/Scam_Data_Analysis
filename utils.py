import re
from datetime import datetime

def parse_date(date='',time=''):
    time_pattern = re.compile(r'^[0-9]+:[0-9]{2}\b')
    date_pattern = re.compile(r'^[0-9]+/[0-9]+/[0-9]{4}')

    try:
        date_str = re.search(date_pattern,date)
        time_str = re.search(time_pattern,time)
    except TypeError:
        return None
        
    # Verify they match the expected pattern
    if not time_str or not date_str:
        return None
    
    # Check if AM or PM
    meridiem_pattern = re.compile(r'\b[Aa]\b')
    match = re.search(meridiem_pattern,time)
    meridiem = ''
    if match:
        meridiem = 'AM'
    else:
        meridiem = 'PM'

    # Parse into datetime object
    dt = datetime.strptime(date_str[0] + ' ' + time_str[0] + ' ' + meridiem, "%m/%d/%Y %I:%M %p")
    return dt

def remove_parenthesis(input=''):
    pattern = re.compile(r'^(\w)+\b')
    
    try:
        match = re.search(pattern,input)
    except TypeError:
        return None
        
    return match[0]
