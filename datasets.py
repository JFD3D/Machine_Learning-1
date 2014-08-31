"""datasets"""
from utils import clean_text, TimeHandler


def csv_to_list(filename):
    """csv file to  ==> data[column][row]"""
    csv = open(filename, 'r')
    fieldnames = clean_text(csv.readline()).split(',')
    print "csv is containing".join(str(e) for e in fieldnames)
    current_line = clean_text(csv.readline())
    data = []
    while current_line != '':
        current_line = clean_text(csv.readline())
        data_row = current_line.split(',')
        data.append(data_row)
    data.pop()
    csv.close()
    return data, fieldnames


def btc_csv_data():
    """ww"""
    days_values, fieldnames = csv_to_list('datasets/csv/btc.csv')
    time_handler = TimeHandler(days_values[0][0])
    days = []
    values = []
    for day_val in days_values:
        days.append([time_handler.date_to_days(day_val[0])])
        values.append(float(day_val[1]))
    return days, values, fieldnames
