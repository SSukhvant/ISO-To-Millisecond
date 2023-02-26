import json
import datetime

# read the JSON file
with open('data-2.json', 'r') as f:
    data1 = json.load(f)
    data = data1['data']

# extract the timestamp from the JSON data
iso_timestamp = data['timestamp']

# convert the ISO formatted timestamp to milliseconds
dt = datetime.datetime.fromisoformat(iso_timestamp)
print(dt)
milliseconds = int(dt.timestamp() * 1000)

# create a dictionary with the timestamp value
result = {'timestamp': milliseconds}

# write the dictionary to a JSON file
with open('data-result.json', 'w') as f:
    json.dump(result, f)

print('Result saved to data-result.json')
