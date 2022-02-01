# Author: Ifeoluwa Ale
# Description: This program reads data from a tree-ring CSV data set and prints the file header.
#              It can also process the data and print some summary statistics, including mean
#              and median data
import csv

def main():
    file = open(input("Enter file name: "), "r")

    csvreader = csv.reader(file)

    header = next(csvreader)
    print("\nFirst line/header:")
    print(" ".join(header) + "\n")

    identifiers = header
    series_data = get_series_data(identifiers[1:])

    line_no = 0
    for row in csvreader:
        if line_no == 0:
            year_1 = int(row[0])

        for i, data in enumerate(row):
            try:
                num = float(data)
                if i != 0:
                    record_data(series_data, identifiers, year_1, 
                            line_no, i, num)
            except ValueError:
                num = 0
        line_no += 1
    
    print_command = input("Would you like to see summary stats of the data? (yes/no)\n")

    if print_command == "yes":
        print_stats(series_data)

    file.close()

# This function arranges the series data into a dictionary where it is 
# stored in a format that makes processing easy
def get_series_data(id_array):
    dictionary = {}
    
    for id in id_array:
        dictionary[id] = ["first", "last", 0, 0, []]
    
    return dictionary

# This function stores data from the time series in a dictionary
# as the program reads from the input file
def record_data(series_data, identifiers, year_1, line, col, data):

    if series_data[identifiers[col]][0] == "first":
        series_data[identifiers[col]][0] = year_1 + line
    
    series_data[identifiers[col]][1] = year_1 + line

    series_data[identifiers[col]][2] += 1

    series_data[identifiers[col]][3] += float(data)

    series_data[identifiers[col]][4].append(data)

# This function calculates the mean of a set of values, given the
# sum of all the values and the number of values in the set
def get_mean(sum, no_vals):
    return "{:.3f}".format(sum/no_vals)

# This function finds the median of a list, given a list of values
# and the length of the list
def get_median(values, array_len):
    sorted_vals = sorted(values)

    if array_len % 2 == 0:
        midpoint = array_len//2
        result = (sorted_vals[midpoint] + sorted_vals[midpoint + 1])/2
    else:
        midpoint = array_len//2 + 1
        result = sorted_vals[midpoint]
    
    return "{:.2f}".format(result).rjust(6)

# This function prints summary statistics of the time series.
def print_stats(series_data):
    print("\nStatistics:")

    print("series".rjust(10), "first", "last", "year", "mean".rjust(5), "median")

    line = 1
    for key, value in series_data.items():
        print(str(line).ljust(4), end="")
        print(key, str(value[0]).rjust(5), str(value[1]).rjust(4), 
                str(value[2]).rjust(4), get_mean(value[3], value[2]).rjust(4),
                    get_median(value[4], value[2]))
        line += 1
    print()

main()