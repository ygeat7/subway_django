from django.shortcuts import render
import folium
from .models import SubwayStation, BusStation

def index(request):
    return render(request, 'sub_station/index.html')
def sub_render(request, 역이름):

    # 지하철 역이름을 필터로 모델에서 해당 값 가져오기
    subway_st = SubwayStation.objects.filter(stationname=역이름)
    lat = subway_st[0].lat  # 해당 역의 위도
    lon = subway_st[0].lon  # 해당 역의 경도

    # folium 객체 생성, Marker 추가
    figure = folium.Map(location=[lat, lon], zoom_start=17)
    folium.Marker(location=[lat, lon], popup=subway_st[0].stationname, icon=folium.Icon(color='red',icon='star')).add_to(figure)
    folium.CircleMarker(location=[lat,lon], radius=250, color='red', fill_color='red').add_to(figure)

    # 해당 지하철역에 근접한 버스정류장 리스트 생성 및 folium 객체에 Marker 추가
    busst_list = [int(x) for x in subway_st[0].nearbusstno.split(',')]
    for i in busst_list :
        bus_name = BusStation.objects.filter(stationid=i)[0].stationname
        bus_lat = BusStation.objects.filter(stationid=i)[0].lat
        bus_lon = BusStation.objects.filter(stationid=i)[0].lon

        folium.Marker(location=[bus_lat, bus_lon], popup=bus_name).add_to(figure)

    # folium 객체의 _repr_html() 메소드를 통해 html 출력할 수 있도록 객체화
    context = {
        'map': figure._repr_html_(),
        'subname':subway_st[0].stationname,
        'buscnt': int(subway_st[0].nearbusstcnt),
    }

    return render(request, 'sub_station/map.html', context)