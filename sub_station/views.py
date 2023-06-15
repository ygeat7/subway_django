from django.shortcuts import render
import folium
from .models import SubwayStation, BusStation, SubTr
import plotly.express as px
import pandas as pd
from datetime import datetime

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
    # folium.CircleMarker(location=[lat,lon], radius=250, color='red', fill_color='red').add_to(figure)

    # 해당 지하철역에 근접한 버스정류장 리스트 생성 및 folium 객체에 Marker 추가
    busst_list = [int(x) for x in subway_st[0].nearbusstno.split(',')]
    for i in busst_list :
        bus_name = BusStation.objects.filter(stationid=i)[0].stationname
        bus_lat = BusStation.objects.filter(stationid=i)[0].lat
        bus_lon = BusStation.objects.filter(stationid=i)[0].lon

        folium.Marker(location=[bus_lat, bus_lon], popup=bus_name).add_to(figure)

    chart, message = sub_tr_plot(역이름)

    # folium 객체의 _repr_html() 메소드를 통해 html 출력할 수 있도록 객체화
    context = {
        'map': figure._repr_html_(),
        'subname':subway_st[0].stationname,
        'buscnt': int(subway_st[0].nearbusstcnt),
        'chart': chart,
        'message': message,
    }

    return render(request, 'sub_station/map.html', context)

def sub_tr_plot(역이름):

    # 지하철 역이름을 필터로 모델에서 해당 값 가져오기
    queryset = SubTr.objects.filter(st_name=역이름)
    sub_df = pd.DataFrame.from_records(queryset.values())

    get_in_col = [x for x in sub_df.columns if '_getin' in x]
    get_out_col = [x for x in sub_df.columns if '_getout' in x]

    tmp1 = sub_df[get_in_col].mean()
    tmp2 = sub_df[get_out_col].mean()
    tmp1.index = [(x.split('_')[1]+'_'+x.split('_')[2]) for x in tmp1.index]
    tmp2.index = [(x.split('_')[1]+'_'+x.split('_')[2]) for x in tmp2.index]
    tmp_df = pd.DataFrame({'승차인원': tmp1, '하차인원': tmp2})

    total_mean = (tmp1 + tmp2).mean()

    now_hour = [x for x in tmp_df.index if str(datetime.now().hour) in x]
    get_in_cong = tmp1.loc[now_hour].mean()
    get_out_cong = tmp2.loc[now_hour].mean()

    if (get_in_cong >= total_mean)|(get_out_cong >= total_mean):
        message = '현재 해당역은 혼잡한 시간대 입니다.'
    else:
        message = '현재 해당역은 한산한 시간대 입니다.'

    fig = px.line(tmp_df, x=tmp_df.index, y=['승차인원', '하차인원'])
    fig.add_hline(y=total_mean, line=dict(color='red', dash='dash'), name='평균승하차인원수')
    fig.update_layout(
        height=500,  # 그래프의 높이 설정 (픽셀 단위)
        width=800,  # 그래프의 너비 설정 (픽셀 단위)
        # legend=dict(
        #     x=0.9,  # 범례의 가로 위치 (0~1 사이의 값)
        #     y=1.0,  # 범례의 세로 위치 (0~1 사이의 값)
        #     xanchor='center',  # 범례 위치를 x축의 중앙에 맞춤
        #     yanchor='top',  # 범례 위치를 y축의 상단에 맞춤
        # ),
        xaxis_title='시간대',
        yaxis_title='인원수',
        xaxis_tickangle=45,
        title_font=dict(size=20),
        paper_bgcolor='white'
    )

    return fig.to_html(), message