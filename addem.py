from time import strftime
def add(a, b):
    return a + b
a=3
b=4
print(f"The sum is {add(a, b)}")

import requests

# Replace with your Tomorrow.io API key
API_KEY = "CR97UqteIZC1gKXDeZqUgYUNfeL3B130"

# Replace with the desired location's latitude and longitude
LOCATION = "king of prussia"

# Make an API request to get weather forecast
url = f"https://api.tomorrow.io/v4/weather/realtime?location={LOCATION}&units=imperial&apikey={API_KEY}"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)

# Print the response
# print(response.text)


print("Weather Forecast")
print("================")
# t = response.json()['data']['timelines'][0]['intervals'][0]['values']['temperature']

results = response.json()['data']
prec=(results['values']['precipitationProbability'])
temp=(results['values']['temperature'])
loc=(response.json()['location']['name'])
print(f"Temperature  {temp}")
print(f"Precipitation {prec}")
print(f"Location {loc}")
    # print("On",date,"it will be", temp, "F")
# response={"data":{"time":"2024-04-07T04:18:00Z","values":{"cloudBase":999,"cloudCeiling":999,"temp":55}}}
# Print the response
# print(response.text)

# print("Weather Forecast")
# print("================")
# t = response.json()['data']['values']['temperature']
# print(t)
# results = response['data']
# print(results['values']['temp'])

my_values = ('temperature','humidity' )
for a,value in enumerate(results['values']):
    if value in my_values:
        print(value,results['values'][value])
        with open('log.txt', 'a') as f:
            f.write(value)
            f.write('  ')
            f.write(str(results['values'][value]))
            f.write('\n')
            formatted_time = strftime("%m-%d-%Y %H:%M:%S")
            f.write(formatted_time)
            f.write('\n')


        