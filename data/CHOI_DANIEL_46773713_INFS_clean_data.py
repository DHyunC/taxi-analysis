import csv

# Input file path
input_file = './data/train.csv'

count = 0
# Open input file
with open(input_file, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    trip_ids= []
    threshold = 0.05
    # Iterate over each row in the CSV file
    for row in reader:
        # Print the value of the 'polyline' column
        polyline_id = row['TRIP_ID']
        polyline_str = row['POLYLINE']
        polyline = eval(polyline_str)
        for i in range(len(polyline) - 1):
            
            if abs(polyline[i][0] - polyline[i+1][0]) > threshold or abs(polyline[i][1] - polyline[i+1][1]) > threshold:
                count += 1
                print("count of problematic records: ",count)
                print("Trip id: ",polyline_id, " found problem coordinates: ", polyline[i], " and ", polyline[i+1])
                trip_ids.append(polyline_id)
                break
        
print("problematic ids: ", trip_ids)