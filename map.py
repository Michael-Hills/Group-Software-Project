import folium


#create map object
lat = 50.735805
long = -3.533051
location = [lat, long]

#map that is bounded to Exeter Uni
map = folium.Map(location = location,
                 min_lon=-3.520532,
                 max_lon=-3.548116,
                 min_lat=50.729748,
                 max_lat=50.741780,
                 max_bounds=True,
                 zoom_start = 16,
                 min_zoom = 15)

#tooltip
tooltip = 'Click for more info'

#create markers:
folium.Marker(location,
    popup="<strong>Exeter Uni</strong>",
    tooltip=tooltip,
    max_bounds=True).add_to(map)

#generate map
map.save('map.html')