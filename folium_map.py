import folium

# Create a map centered at a specific location
m = folium.Map(location=[28.419701, -81.583546], zoom_start=12)

# Add a marker
folium.Marker([28.419701, -81.583546], popup="Montana").add_to(m)

# Save to HTML file
m.save("map.html")
