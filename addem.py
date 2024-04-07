a=3
b=4
print(f"The sum is {a+b}")

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
print(response.text)


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
# t = response.json()['data']['timelines'][0]['intervals'][0]['values']['temperature']

# results = response['data']
# print(results['values']['temp'])


    # 40.10538439053338, -75.41601923360118
    # curl --request GET --url 'https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466&apikey=CR97UqteIZC1gKXDeZqUgYUNfeL3B130'