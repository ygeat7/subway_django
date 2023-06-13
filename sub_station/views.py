from django.shortcuts import render
import folium
import math
from .models import SubwayStation, BusStation

def sub_render(request, 역이름):

    subway_st = SubwayStation.objects.filter(stationname=역이름)
    lat = subway_st[0].lat
    lon = subway_st[0].lon

    figure = folium.Map(location=[lat, lon], zoom_start=17)
    folium.Marker(location=[lat, lon], popup=subway_st[0].stationname).add_to(figure)

    busst_list = [int(x) for x in subway_st[0].nearbusstno.split(',')]
    for i in busst_list :
        bus_name = BusStation.objects.filter(stationid=i)[0].stationname
        bus_lat = BusStation.objects.filter(stationid=i)[0].lat
        bus_lon = BusStation.objects.filter(stationid=i)[0].lon

        folium.Marker(location=[bus_lat, bus_lon], popup=bus_name).add_to(figure)

    context = {
        'map': figure._repr_html_()
    }

    return render(request, 'sub_station/map.html', context)