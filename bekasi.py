import folium

aryaniken = folium.Map(
    location=[-6.226695, 106.996265],
    zoom_start=12,
    tiles='Stamen Terrain'
)

tooltip = 'Click me!'

folium.Marker([-6.330075, 107.011625], popup='<i>Bekasi Timur Regency 3</i>').add_to(aryaniken)
folium.Marker([-6.316507, 107.009242], popup='<i>SMPN 10 Bekasi</i>').add_to(aryaniken)
folium.Marker([-6.320767, 107.016391], popup='<i>KFC Zambrud</i>').add_to(aryaniken)
folium.Marker([-6.324403, 107.015596], popup='<i>SDN Cimuning 3</i>').add_to(aryaniken)
folium.Marker([-6.256254, 106.992955], popup='<i>Lottemart Bekasi</i>').add_to(aryaniken)
folium.Marker([-6.242567, 106.999776], popup='<i>Taman Kota Bekasi</i>').add_to(aryaniken)
folium.Marker([-6.242488, 106.999878], popup='<i>Alun-alun Kota Bekasi</i>').add_to(aryaniken)
folium.Marker([-6.242775, 107.000325], popup='<i>Gedung Sartika</i>').add_to(aryaniken)
folium.Marker([-6.244090, 106.999518], popup='<i>Polres Metro Kota Bekasi</i>').add_to(aryaniken)
folium.Marker([-6.246491, 107.004786], popup='<i>STIKES Bani Saleh</i>').add_to(aryaniken)

import folium

rifa = folium.Map(location=[-6.241586,  106.992416],zoom_start=10,)
folium.Marker(location=[-6.173932, 106.972844],popup='Medan Satria',icon=folium.Icon(icon='info-sign')).add_to(rifa)
folium.Marker(location=[-6.263362, 106.908820],popup='Jaticempaka',icon=folium.Icon(icon='info-sign')).add_to(rifa)
folium.Marker(location=[-6.386206, 106.914999],popup='Jatikarya',icon=folium.Icon(icon='info-sign')).add_to(rifa)
folium.Marker(location=[-6.352086, 106.935599],popup='Jatirangga',icon=folium.Icon(icon='info-sign')).add_to(rifa)
folium.Marker(location=[-6.326835, 106.998770],popup='Padurenan',icon=folium.Icon(icon='info-sign')).add_to(rifa)
folium.Marker(location=[-6.233329, 107.024176],popup='Bekasi Timur',icon=folium.Icon(icon='info-sign')).add_to(rifa)
folium.Marker(location=[-6.318646, 106.952765],popup='Jatiluhur',icon=folium.Icon(icon='info-sign')).add_to(rifa)
folium.Marker(location=[-6.223090, 107.004950],popup='Marga Mulya',icon=folium.Icon(icon='info-sign')).add_to(rifa)
folium.Marker(location=[-6.328883, 106.953452],popup='Jatisari',icon=folium.Icon(icon='info-sign')).add_to(rifa)
folium.Marker(location=[-6.341167, 107.003577],popup='Bantar Gebang',icon=folium.Icon(icon='info-sign')).add_to(rifa)
