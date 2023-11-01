import requests
import json
import matplotlib.pyplot as plt

api_key = '3ebf83d2d6644224ab975149232010'

city = input("Enter the name of the City\n")

url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

r = requests.get(url)
weather_dic = json.loads(r.text)

w_c = weather_dic['current']['temp_c']
w_f = weather_dic['current']['temp_f']
w_feelslike = weather_dic['current']['feelslike_c']
w_humidity = weather_dic['current']['humidity']

# Create a bar chart
data = [w_c, w_f, w_feelslike, w_humidity]
labels = ['Temperature (°C)', 'Temperature (°F)', 'Feels Like (°C)', 'Humidity (%)']
x = range(len(data))

plt.bar(x, data, tick_label=labels, color=['blue', 'red', 'green', 'orange'])

plt.xlabel("Weather Data")
plt.ylabel("Value")
plt.title(f"Weather Information for {city}")
plt.ylim(0, max(data) + 10)  # Adjust the y-axis range

# Display the values on top of the bars
for i, value in enumerate(data):
    plt.text(i, value, str(value), ha='center', va='bottom')

plt.show()
