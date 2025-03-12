from geopy.geocoders import Nominatim
import pandas as pd

import folium

def get_coordinates(place, zip):
    # Point GeoPy to your local Nominatim instance
    geolocator = Nominatim(user_agent="my-app", scheme="http", timeout=10)

    # Geocode an address
    location = geolocator.geocode(f"{place}, {zip}")
    if location:
        print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
        return location.latitude, location.longitude
    else:
        print("Location not found")
        return None




# Create a map centered at a specific location
m = folium.Map(location=[28.419701, -81.583546], zoom_start=12)

df = pd.read_csv("locations.csv")

for row in df.iloc:
    # Get the coordinates
    coors = get_coordinates(row['place'], row['somethingzip'])

    # Add a marker
    folium.Marker([coors[0], coors[1]], popup="").add_to(m)

    df["lat"] = coors[0]
    df["lon"] = coors[1]

df.to_csv("updated_locations.csv", index=False)





# # Save to HTML file
m.save("map.html")