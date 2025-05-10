import requests
import folium

# Constants
WEATHER_API_KEY = "3f31e4e5a662be8502aa088b158b9f83"  # Your OpenWeatherMap API Key
ALL_ROAD_CAMS_URL = "https://allroadcams.com/"  # Placeholder; no direct API assumed

# Function to get weather alerts for a specific area
def get_weather_alerts(lat, lon):
    """
    Fetches weather alerts using OpenWeatherMap API for a given latitude and longitude.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data:", response.status_code)
        return None

# Example traffic cameras (replace this with actual camera data if available)
traffic_cameras = [
    {"name": "Camera 1", "lat": 34.0522, "lon": -118.2437},  # Los Angeles
    {"name": "Camera 2", "lat": 40.7128, "lon": -74.0060},  # New York
    {"name": "Camera 3", "lat": 41.8781, "lon": -87.6298},  # Chicago
]

# Create a map centered over the USA
map = folium.Map(location=[39.8283, -98.5795], zoom_start=5)

# Add traffic cameras and associated weather alerts to the map
for camera in traffic_cameras:
    weather = get_weather_alerts(camera["lat"], camera["lon"])
    weather_info = (
        f"Weather: {weather['weather'][0]['description']}\n"
        f"Temperature: {weather['main']['temp']}K\n"
        f"Humidity: {weather['main']['humidity']}%"
        if weather
        else "No weather data available"
    )
    folium.Marker(
        [camera["lat"], camera["lon"]],
        popup=f"{camera['name']}\n{weather_info}",
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(map)

# Save the map to an HTML file
map.save("traffic_weather_map.html")
print("Map saved as traffic_weather_map.html")
