from datetime import datetime
import calendar
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--year',
                        '-y',
                        type=int, default=datetime.today().year,
                        help='Choose the year. Default is the current year.')
    parser.add_argument('--month',
                        '-m',
                        type=int, default=datetime.today().month,
                        help='Choose the month. Default is the current month.') 
    parser.add_argument('--genyear',
                        action='store_true', default=False,
                        help='Generate the whole year') 
    args = parser.parse_args()
    return args

def generate_month(year, month):
    week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    markdown_str = '|' + '|'.join(week) + '|\n' + \
                   '|' + ''.join([':-:|' for _ in range(7)]) + '\n'

    for days in calendar.Calendar().monthdatescalendar(year, month):
        markdown_str += '|' + '|'.join([str(d.day) for d in days]) + '|\n'
    return markdown_str

def print_calendar(year, month):
    print(calendar.month(year, month).split('\n', 1)[0])
    print(generate_month(year, month))
    pass

def generate_whole_year(year):
    for month in range(1, 13):
        print_calendar(year, month)
    pass

    
args = get_args()
year = args.year
month = args.month
if args.genyear:
    generate_whole_year(year)
else:
    print_calendar(args.year, args.month)
