import geopandas as gpd
import matplotlib.pyplot as plt

# Load the dataset manually
world = gpd.read_file("https://naturalearth.s3.amazonaws.com/10m_cultural/ne_10m_admin_0_countries.zip")

# Create a point at New York coordinates
points = gpd.GeoDataFrame(geometry=gpd.points_from_xy([-74.0060], [40.7128]))

# Plot the map
fig, ax = plt.subplots(figsize=(10, 6))
world.plot(ax=ax, color="lightgrey")
points.plot(ax=ax, color="red", markersize=100)
plt.show()
