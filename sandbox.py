from pyproj import Proj, transform

# Define the UTM and WGS84 projections
utm_proj = Proj(proj='utm', zone=12, ellps='WGS84')  # Replace 'zone=33' with your specific UTM zone
wgs84_proj = Proj(proj='latlong', datum='WGS84')

# Example UTM coordinates (easting, northing)
utm_easting = 500000
utm_northing = 4649776

# Convert UTM to WGS84
longitude, latitude = transform(utm_proj, wgs84_proj, utm_easting, utm_northing)

print(f"Latitude: {latitude}, Longitude: {longitude}")

