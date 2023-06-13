from django.db import models

class BusStation(models.Model):
    stationid = models.IntegerField(blank=True, null=True)
    stationname = models.TextField(blank=True, null=True)
    stationtype = models.TextField(blank=True, null=True)
    stationno = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_station'

    def __str__(self):
        return f'[버스 : {self.stationid}] {self.stationname}'

class SubwayStation(models.Model):
    stationid = models.IntegerField(blank=True, null=True)
    stationname = models.TextField(blank=True, null=True)
    stationno = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    nearbusstcnt = models.FloatField(blank=True, null=True)
    nearbusstno = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subway_station'

    def __str__(self):
        return f'[지하철 : {self.stationid}] {self.stationname}'