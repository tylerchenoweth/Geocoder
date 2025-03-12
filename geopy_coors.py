from geopy.geocoders import Nominatim

# Point GeoPy to your local Nominatim instance
geolocator = Nominatim(user_agent="my-app", scheme="http", timeout=10)

# Geocode an address
location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
if location:
    print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
else:
    print("Location not found")