from pyproj import Proj, transform
import os

def get_gcp_array(path):
    lines = []
    with open(path, 'r') as file:
        for line in file:
            formatted_line = []
            for el in line.split(' '):
                try:
                    formatted_line.append(float(el.strip()))
                except:
                    formatted_line.append(el.strip())

            if type(formatted_line[1]) == float:
                lines.append(formatted_line)

    return lines


# Define the UTM and WGS84 projections
utm_proj = Proj(proj='utm', zone=12, ellps='WGS84')  # Replace 'zone=33' with your specific UTM zone
wgs84_proj = Proj(proj='latlong', datum='WGS84')

root_path = r'C:\Users\MeyerTaffel\local\coding\GCP_scripting'
gcp_list_filename = r'gcp_list.txt'
gcps = get_gcp_array(os.path.join(root_path, gcp_list_filename))
print(gcps)

for gcp in gcps:
    gcp[0], gcp[1] = transform(utm_proj, wgs84_proj, gcp[0], gcp[1])

gcps.insert(0, ["EPSG:4326"])

filename = "gcp_list_geographic.txt"
with open(os.path.join(root_path, filename), 'w') as file:
    for gcp in gcps:
        file.write(" ".join(str(el) for el in gcp) + "\n")
print(f"File '{filename}' created successfully.")

