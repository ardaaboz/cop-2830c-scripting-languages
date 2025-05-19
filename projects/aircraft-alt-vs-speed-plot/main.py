import matplotlib.pyplot as plt
import csv

# Safely opening and closing csv file
with open('alt_vs_speed.csv', 'r') as csvfile:
    # Reading each line
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row

    # Creating the lists
    altitude_list = []
    mach_number_list = []
    mph_value_list = []

    for row in reader:
        # Skip the rows with empty values
        if row[0].strip() == '' or row[1].strip() == '':
            continue

        # Add values to lists
        altitude_list.append(float(row[0]))
        mach_number_list.append(float(row[1]))

    # Convert mach numbers to mph
    for mach in mach_number_list:
        mph_value = mach * 767.269
        mph_value_list.append(mph_value)

    # Create and show the scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(altitude_list, mph_value_list, s = 10,color = '#000000')
    plt.title("Altitude vs Miles per Hour")
    plt.xlabel("Altitude (ft)")
    plt.ylabel("Miles per Hour")
    plt.grid(True)
    plt.show()