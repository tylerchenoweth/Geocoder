import requests
import folium
import csv

def get_coordinates(place, zip):
    # Base URL
    url = "https://nominatim.openstreetmap.org/search"

    # Query parameters
    params = {
        "q": f"{place}, {zip}",  # Example address
        "format": "json",  # Return data in JSON format
        "addressdetails": 1,  # Include address details
        "limit": 1  # Return only one result
    }

    # Custom user-agent header (replace with your identifier)
    headers = {
        "User-Agent": "MyApp/1.0 (your.email@example.com)"  # Replace with your email or app name
    }

    # Make the API call
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the JSON response
        data = response.json()
        if data:
            result = data[0]
            lat = result["lat"]
            lon = result["lon"]
            # print(f"Coordinates: \nLatitude {lat}, \nLongitude {lon}\n")
            if "address" in result:
                address = result['address']
            else:
                address = None

            return lat,lon,result['address']
        else:
            print("No results found")

            return None

    except requests.exceptions.RequestException as e:
        print(f"Error making API call: {e}")

        return None



# coors = get_coordinates("Fairway Oaks CT", 21074) 

# print(coors[0])

# Create a map centered at a specific location
m = folium.Map(location=[28.419701, -81.583546], zoom_start=12)

with open("locations.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        coors = get_coordinates(row["place"], row['somethingzip'])
        folium.Marker([coors[0], coors[1]], popup=coors[2]['road']).add_to(m)

# Save to HTML file
m.save("map.html")